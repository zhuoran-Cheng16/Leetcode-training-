
'''

SELECT a.*,b.min_issue
    FROM(
      SELECT
        `source` AS `data_source`,
        `signal`,
        `time_type`,
        `geo_type`,
        MIN(`time_value`) AS `min_time`,
        MAX(`time_value`) AS `max_time`,
        COUNT(DISTINCT `geo_value`) AS `num_locations`,
        MIN(`value`) AS `min_value`,
        MAX(`value`) AS `max_value`,
        ROUND(AVG(`value`),7) AS `mean_value`,
        ROUND(STD(`value`),7) AS `stdev_value`,
        MAX(`value_updated_timestamp`) AS `last_update`,
        MAX(`issue`) as `max_issue`,
        MIN(`lag`) as `min_lag`,
        MAX(`lag`) as `max_lag`
    FROM
        `covidcast` use index (for_metadata) 
    WHERE
        `source` = 'jhu-csse' AND
        `signal` ='deaths_7dav_incidence_prop             ' 
    GROUP BY
        `time_type`,
        `geo_type`    
    ORDER BY
        `time_type` ASC,
        `geo_type` ASC 
    )a
    JOIN(
      SELECT        
        `time_type`,
        `geo_type`,          
        MIN(`issue`) as `min_issue`
      FROM 
        `covidcast` 
      WHERE
        `source` = 'jhu-csse' AND
        `signal` ='deaths_7dav_incidence_prop             ' 
      GROUP BY
        `time_type`,
        `geo_type`    
      ORDER BY
        `time_type` ASC,
        `geo_type` ASC 
    )b
    ON 
      a.`geo_type`=b.`geo_type` AND
      a.`time_type`=b.`time_type`
;
'''

'''

  SELECT
        `source` AS `data_source`,
        `signal`,
        `time_type`,
        `geo_type`,
        MIN(`time_value`) AS `min_time`,
        MAX(`time_value`) AS `max_time`,
        COUNT(DISTINCT `geo_value`) AS `num_locations`,
        MIN(`value`) AS `min_value`,
        MAX(`value`) AS `max_value`,
        ROUND(AVG(`value`),7) AS `mean_value`,
        ROUND(STD(`value`),7) AS `stdev_value`,
        MAX(`value_updated_timestamp`) AS `last_update`,
        MAX(`issue`) as `max_issue`,
        MIN(`lag`) as `min_lag`,
        MAX(`lag`) as `max_lag`
    FROM
        `covidcast` use index (for_metadata) 
    WHERE
        `source` = 'jhu-csse' AND
        `signal` ='deaths_7dav_incidence_prop' 
    GROUP BY
        `time_type`,
        `geo_type`    
    ORDER BY
        `time_type` ASC,
        `geo_type` ASC;

 
       
       
        '''