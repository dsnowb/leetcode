SELECT sub.score Score, CAST(sub.rank AS UNSIGNED) Rank FROM (
    SELECT
        @rank := IF(@score = Score, IF(@rank = 0, 1, @rank), @rank + 1) rank,
        @score := Score score
    FROM
        Scores,
        (SELECT @rank := 0, @score := 1) var
    ORDER BY Score DESC
) sub;
