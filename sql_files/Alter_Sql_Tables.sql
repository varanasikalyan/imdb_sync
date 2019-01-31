USE imdb
GO

ALTER TABLE dbo.namebasics
ALTER COLUMN nconst VARCHAR(20) NOT NULL

ALTER TABLE dbo.namebasics
ALTER COLUMN primaryName VARCHAR(256) NOT NULL

ALTER TABLE dbo.namebasics
ALTER COLUMN birthYear VARCHAR(5) NOT NULL

ALTER TABLE dbo.namebasics
ALTER COLUMN deathYear VARCHAR(5) NOT NULL

ALTER TABLE dbo.namebasics
ADD PRIMARY KEY(nconst)

CREATE INDEX idx_primary_name
ON dbo.namebasics (primaryName)

ALTER TABLE [dbo].[nameprimaryprofession]
ALTER COLUMN nconst VARCHAR(20) NOT NULL

ALTER TABLE [dbo].[nameprimaryprofession]
ALTER COLUMN primaryProfession VARCHAR(256)

CREATE INDEX idx_primary_profession
ON [dbo].[nameprimaryprofession] (primaryProfession)

ALTER TABLE [dbo].[nameknownfortitles]
ALTER COLUMN nconst VARCHAR(20) NOT NULL

ALTER TABLE [dbo].[nameknownfortitles]
ALTER COLUMN [knownForTitles] VARCHAR(256)

CREATE INDEX idx_known_for_titles
ON [dbo].[nameknownfortitles] ([knownForTitles])