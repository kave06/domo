SELECT
  value,
  t_time
FROM reading R
  INNER JOIN (
               SELECT
                 DATE(time) t_date,
                 MIN(time)  t_time
               FROM reading
               GROUP BY DATE(time), HOUR(time)
               HAVING t_date BETWEEN '2017-08-01' AND '2017-08-01'
             ) T ON T.t_time = R.time;
