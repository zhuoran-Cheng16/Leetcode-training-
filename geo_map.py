#csv文件路线 A dictionary of the filenames for the crosswalk tables.
CROSSWALK_FILEPATHS={"fips","zip","state","state_code","state_id",
                    "state_name","hhs","nation", "jhu_uid"} 
DATA_PATH = "data"
#nation->state
#state->county
#hhr->state
class GeoMapper:
    '''“Delphi 中常用的地理映射工具。

        GeoMapper 类提供了用于在不同地理编码。支持的地理编码geocode：
        - zip: zip5，长度为 5 的 0-9 字符串，前导 0
        - fips：州代码和县代码，长度为 5 str 的 0-9 前导 0
        - msa：大都市统计区，长度为 5 的 0-9 字符串，前导 0
        - state_code：状态代码，0-9 的 str
        - state_id：状态 ID，A-Z 的字符串
        - hrr：医院转诊区域，int 1-500

        Mappings:
        - [x] zip -> fips : population weighted
        - [x] zip -> hrr : unweighted
        - [x] zip -> msa : unweighted
        - [x] zip -> state
        - [x] zip -> hhs
        - [x] zip -> population
        - [x] state code -> hhs
        - [x] fips -> state : unweighted
        - [x] fips -> msa : unweighted
        - [x] fips -> megacounty
        - [x] fips -> hrr
        - [x] fips -> hhs
        - [x] nation
        - [ ] zip -> dma (postponed)

        GeoMapper 实例从包 data_dir 加载crosswalk tables, 这
        假设crosswalk tables是使用 geo_data_proc.py 脚本构建的
        在 data_proc/geomap 中。如果代码之间的映射不是一对多，则该表具有
        只有两列。如果映射是一对多，那么第三列，权重列，
        存在（例如 zip、fips、weight；满足 (sum(weights) where zip==ZIP) == 1）

        示例用法
        ==========
        主要的 GeoMapper 对象按需加载和存储crosswalk dataframes。

        用新的地理编码替换地理编码时，会对数据列执行聚合步骤
        合并条目（即在多对一映射或加权映射的情况下）。这
        需要数据列的规范，这些列被假定为所有列
        不是 date_col 中指定的地理编码或日期列。

        示例 1：添加具有新地理编码（可能具有权重weights）的新列：
        > gmpr = GeoMapper()
        > df = gmpr.add_geocode(df, "fips", "zip", from_col="fips", new_col="geo_id",
        date_col="timestamp", dropna=False)

        示例 2：用新的地理编码列替换地理编码列，用权重聚合数据：
        > gmpr = GeoMapper()
        > df = gmpr.replace_geocode(df, "fips", "zip", from_col="fips", new_col="geo_id",
        date_col="timestamp", dropna=False)
'''
    def __init__(self):
        """Initialize geomapper.
        从crosswalks dir中导出path，分配不同的geo code， 
        将geo type导入geo list 
        Holds loading the crosswalk tables until a conversion function is first used.
        保持加载crosswalk tables，直到第一次使用转换函数。
        Parameters
        ---------
        crosswalk_files : dict
            A dictionary of the filenames for the crosswalk tables.
        """
    
    def _load_crosswalk(self, from_code, to_code):
     #加载crosswalk from from_code -> to_code.
     
     assert from_code in self.crosswalk_filepaths #前缀
     assert to_code in self.crosswalk_filepaths[from_code] #后缀
     return self.crosswalks[from_code][to_code]

    def _load_crosswalk_from_file(self, from_code, to_code):
        #不同file 类型表示不同read——csv格式 包括to code-》pop
        # Weighted crosswalks
        if (from_code, to_code) in [
            ("zip", "fips"),
            ("fips", "zip"),
            ("jhu_uid", "fips"),
            ("zip", "msa"),
            ("fips", "hrr"),
            ("zip", "hhs")
        ]:
            dtype = {
                from_code: str,
                to_code: str,
                "weight": float,
            }
        # Unweighted crosswalks
        elif (from_code, to_code) in [
            ("zip", "hrr"),
            ("fips", "msa"),
            ("fips", "hhs"),
            ("state_code", "hhs")
        ]:
            dtype = {from_code: str, to_code: str}

        # Special table of state codes, state IDs, and state names
        elif (from_code, to_code) == ("state", "state"):
            dtype = {
                "state_code": str,
                "state_id": str,
                "state_name": str,
            }
        elif (from_code, to_code) == ("zip", "state"):
            dtype = {
                "zip": str,
                "weight": float,
                "state_code": str,
                "state_id": str,
                "state_name": str,
            }
        elif (from_code, to_code) == ("fips", "state"):
            dtype = {
                    "fips": str,
                    "state_code": str,
                    "state_id": str,
                    "state_name": str,
            }

        # Population tables
        elif to_code == "pop":
            dtype = {
                from_code: str,
                "pop": int,
            }
            usecols = [
                from_code,
                "pop"
            ]
        return pd.read_csv(stream, dtype=dtype, usecols=usecols)
    
    def megacounty_creation(
        data,
        thr_count,
        thr_win_len,
        thr_col="visits",
        fips_col="fips",
        date_col="date",
        mega_col="megafips",
    ):
     """Create megacounty column.
        Parameters
        ---------
        data: pd.DataFrame input data
        thr_count: numeric, if the sum of counts exceed this, then fips is converted to mega
        thr_win_len: int, the number of Days to use as an average
        thr_col: str, column to use for threshold
        fips_col: str, fips (county) column to create
        date_col: str, date column (is not aggregated, groupby), if None then no dates
        mega_col: str, the megacounty column to create
        Return
        ---------
        data: copy of dataframe
            A dataframe with a new column, mega_col, that contains megaFIPS (aggregate
            of FIPS clusters) values depending on the number of data samples available.
            数据：数据帧的副本
            具有新列 mega_col 的数据框，其中包含 megaFIPS（聚合FIPS 集群）值取决于可用数据样本的数量。
        """

    def add_geocode(
        self, df, from_code, new_code, from_col=None, new_col=None, dropna=True
    ):
        """Add a new geocode column to a dataframe.
        Currently supported conversions:
        - fips -> state_code, state_id, state_name, zip, msa, hrr, nation, hhs
        - zip -> state_code, state_id, state_name, fips, msa, hrr, nation, hhs
        - jhu_uid -> fips
        - state_x -> state_y (where x and y are in {code, id, name}), nation
        - state_code -> hhs, nation
        Parameters
        ---------
        df: pd.DataFrame
            Input dataframe.
        from_code: {'fips', 'zip', 'jhu_uid', 'state_code', 'state_id', 'state_name'}
            Specifies the geocode type of the data in from_col.
        new_code: {'fips', 'zip', 'state_code', 'state_id', 'state_name', 'hrr', 'msa',
                   'hhs'}
            Specifies the geocode type in new_col.
        from_col: str, default None
            Name of the column in dataframe containing from_code. If None, then the name
            is assumed to be from_code.
        new_col: str, default None
            Name of the column in dataframe containing new_code. If None, then the name
            is assumed to be new_code.
        dropna: bool, default False
            Determines how the merge with the crosswalk file is done. If True, the join is inner,
            and if False, the join is left. The inner join will drop records from the input database
            that have no translation in the crosswalk, while the outer join will keep those records
            as NA.
        Return
        ---------
        df: pd.DataFrame
            A copy of the dataframe with a new geocode column added.
        """
        df=df.copy()

    def add_population_column(self, data, geocode_type, geocode_col=None, dropna=True):
        """
        Append a population column to a dataframe, based on the FIPS or ZIP code.

        If no dataframe is provided, the full crosswalk from geocode to population is returned.

        Parameters
        ---------
        data: pd.DataFrame
            The dataframe with a FIPS code column.
        geocode_type: {"fips", "zip"}
            The type of the geocode contained in geocode_col.
        geocode_col: str, default None
            The name of the column containing the geocodes. If None, uses the geocode_type
            as the name.

        Returns
        --------
        data_with_pop: pd.Dataframe
            A dataframe with a population column appended.
        """