-- SQLite
-- SELECT "title", "author", "year"
-- FROM "longlist"
-- WHERE 2019 <= "year" AND "year" <= 2022

-- SELECT "title", "author", "year"
-- FROM "longlist"
-- WHERE "year" BETWEEN 2019 AND 2022

-- SELECT "title", "rating", "votes"
-- FROM "longlist"
-- WHERE "rating" > 4.0 AND "votes" > 10000

-- SELECT "title", "pages"
-- FROM "longlist"
-- WHERE "pages" < 200

-- SELECT "title", "rating", "votes"
-- FROM "longlist"
-- ORDER BY "rating" DESC, "votes" DESC

-- SELECT ROUND(AVG("rating"), 2) AS "average rating"
-- FROM "longlist"

-- SELECT MAX("rating")
-- FROm "longlist"

-- SELECT SUM("votes")
-- FROm "longlist"

-- SELECT COUNT(*)
-- FROM "longlist"

-- SELECT COUNT(DISTINCT "publisher")
-- FROM "longlist"
