SELECT DISTINCT sub.Num ConsecutiveNums FROM (
    SELECT
        Num,
        @counter := IF(Num = @num, @counter + 1, 1) counter,
        @num := Num
    FROM
        Logs,
        (SELECT @counter := 0, @num := NULL) init
) sub
WHERE
    sub.counter = 3;
