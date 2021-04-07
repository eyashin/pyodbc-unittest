-- (c) Evgeny Yashin 2001
-- example script for pyodbc-unittest library
-- for SAP/SYBASE or MS SQL

SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[VERSION](
    [VersionNumber] [varchar](10) NOT NULL,
    [Actual] [char](10) NULL,
CONSTRAINT [PK_VERSION] PRIMARY KEY CLUSTERED
(
    [VersionNumber] ASC
)
)
GO

INSERT INTO [dbo].[VERSION]
           ([VersionNumber]
           ,[Actual])
     VALUES
           ('1.0'
           ,'Y')
GO

CREATE VIEW [dbo].[V_VERSION] AS
SELECT [VersionNumber]
      ,[Actual]
FROM [dbo].[VERSION]
WHERE [Actual] = 'Y'
GO

CREATE PROCEDURE SP_GET_VERSION
AS
BEGIN
    SELECT 'CURRENT VERSION:' AS ReportName
    SELECT [VersionNumber] FROM [dbo].[V_VERSION]

END
GO

CREATE PROCEDURE SP_UPDATE_VERSION (@Version VARCHAR(10))
AS
BEGIN
    UPDATE [dbo].[VERSION] SET [Actual] = Null
    IF NOT exists(SELECT 1 FROM [dbo].[VERSION] WHERE [VersionNumber] = @Version)
        INSERT INTO [dbo].[VERSION]([VersionNumber]) VALUES(@Version)
    UPDATE [dbo].[VERSION] SET [Actual] = 'Y' WHERE [VersionNumber] = @Version
END

GO