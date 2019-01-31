SELECT nb.nconst,
       nb."primaryName",
       nb."birthYear",
       nb."deathYear",
       npp."primaryProfession"
FROM dbo.namebasics AS nb
INNER JOIN dbo.nameprimaryprofession AS npp ON (nb.nconst = npp.nconst)
WHERE nb."primaryName" LIKE 'Marlon Brando'