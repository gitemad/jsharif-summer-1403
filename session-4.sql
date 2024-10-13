-- SQLite
-- SELECT "name" FROM "translators"
-- INTERSECT
-- SELECT "name" FROM "authors"

-- SELECT "name", 'translator' AS "profession" FROM "translators"
-- UNION
-- SELECT "name", 'author' AS "profession" FROM "authors"

-- SELECT "name" FROM "authors"
-- EXCEPT
-- SELECT "name" FROM "translators"

-- SELECT "book_id" FROM "translated"
-- WHERE "translator_id" = (
--     SELECT "id" FROM "translators"
--     WHERE "name" = 'Margaret Jull Costa'
-- )
-- INTERSECT
-- SELECT "book_id" FROM "translated"
-- WHERE "translator_id" = (
--     SELECT "id" FROM "translators"
--     WHERE "name" = 'Sophie Hughes'
-- )

-- SELECT "title", AVG("rating") AS "average rating", COUNT("rating") AS "rating count"
-- FROM "ratings"
-- JOIN "books" ON "ratings"."book_id" = "books"."id"
-- GROUP BY "book_id"

SELECT (
    SELECT "title"
    FROM "books"
    WHERE "id" = "book_id"
) AS "title", AVG("rating") AS "average rating", COUNT("rating") AS "rating count"
FROM "ratings"
GROUP BY "book_id"