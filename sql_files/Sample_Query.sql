SELECT nb.nconst,
       nb."primaryName",
       nb."birthYear",
       nb."deathYear",
       npp."primaryProfession"
FROM public.namebasics AS nb
INNER JOIN public.nameprimaryprofession AS npp ON (nb.nconst = npp.nconst)
WHERE nb."primaryName" LIKE 'Marlon Brando'