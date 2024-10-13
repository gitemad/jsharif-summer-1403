-- SQLite
-- SELECT "title"
-- FROM "books"
-- WHERE "publisher_id" = (
--     SELECT "publisher_id"
--     FROM "publishers"
--     WHERE "publisher" = 'Fitzcarraldo Editions'
-- )

-- SELECT ROUND(AVG("rating"), 2)
-- FROM "ratings"
-- WHERE "book_id" = (
--     SELECT "id"
--     FROM "books"
--     WHERE "title" = 'In Memory of Memory'
-- )

-- SELECT "name"
-- FROM "authors"
-- WHERE "id" = (
--     SELECT "author_id"
--     FROM "authored"
--     WHERE "book_id" = (
--         SELECT "id"
--         FROM "books"
--         WHERE "title" = 'Flights'
--     )
-- )

-- SELECT "title"
-- FROM "books"
-- WHERE "id" IN (
--     SELECT "book_id"
--     FROM "authored"
--     WHERE "author_id" IN (
--         SELECT "id"
--         FROM "authors"
--         WHERE "name" = 'Fernanda Melchor'
--     )
-- )


-- SELECT "b"."title", "p"."publisher", "b"."publisher_id"
-- FROM "books" AS "b"
-- LEFT JOIN "publishers" AS "p"
--     ON "b"."publisher_id" = "p"."publisher_id"

SELECT "books"."title", "translators"."name"
FROM "books"
LEFT JOIN "translated" ON "books"."id" = "translated"."book_id"
LEFT JOIN "translators" ON "translators"."id" = "translated"."translator_id"
ORDER BY "books"."title"