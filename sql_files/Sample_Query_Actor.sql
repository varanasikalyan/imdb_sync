SELECT nb.nconst,
       nb."primaryName",
       tb."primaryTitle",
	   tb."originalTitle",
	   tp.category,
	   tp.characters
FROM public.namebasics AS nb
INNER JOIN public.titleprincipals AS tp ON (nb.nconst = tp.nconst)
INNER JOIN public.titlebasics AS tb ON (tp.tconst = tb.tconst)
WHERE nb."primaryName" LIKE 'Marlon Brando'