-- SQLite
-- SELECT *
-- FROM "longlist";

-- SELECT "title"
-- FROM "longlist";

-- SELECT "title", "author"
-- FROM "longlist"
-- LIMIT 10;

-- SELECT "title", "author", "year"
-- FROM "longlist"
-- WHERE "year" = 2023;

-- SELECT "title", "format"
-- FROM "longlist"
-- WHERE "format" != 'hardcover';

-- SELECT "title", "format"
-- FROM "longlist"
-- WHERE "format" <> 'hardcover';

-- SELECT "title", "format"
-- FROM "longlist"
-- WHERE NOT "format" = 'hardcover';

-- SELECT "title", "author", "year"
-- FROM "longlist"
-- WHERE "year" = 2022 OR "year" = 2023;

-- SELECT "title", "author", "year", "format"
-- FROM "longlist"
-- WHERE ("year" = 2022 OR "year" = 2023) AND "format" != 'hardcover';

-- SELECT "title", "translator"
-- FROM "longlist"
-- WHERE "translator" IS NULL

-- SELECT "title", "translator"
-- FROM "longlist"
-- WHERE "translator" IS NOT NULL

-- SELECT "title"
-- FROM "longlist"
-- WHERE "title" LIKE '%love%';

-- SELECT "title"
-- FROM "longlist"
-- WHERE "title" LIKE 'the%';

-- SELECT "title"
-- FROM "longlist"
-- WHERE "title" LIKE 'T____________'
