import sqlite3

conn = sqlite3.connect('BHA.db')
print("Opened database successfully")
c = conn.cursor()
# BHAData
c.execute('''CREATE TABLE BHAData
       (ID INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
       CaseFile         CHAR,
       ProductName           CHAR,
       ProductVersion            CHAR,
       SaveDate        CHAR,
       ComputerName         CHAR,
       UserName        CHAR,
       CurrentCulture   CHAR,
       DataVersion     CHAR,
       ClassType      CHAR,
       "Index"          INT);''')

# General
c.execute('''create table General
(
  ID    INTEGER PRIMARY KEY  AUTOINCREMENT   not null,
  BHA_ID            INTEGER     not null
    constraint BHA_ID
    references BHAData,
  CaseFile          CHAR,
  ClassType         CHAR    not null,
  Date              CHAR    not null,
  Operator          CHAR,
  Well              CHAR,
  Field             CHAR,
  Rig               CHAR,
  Country           CHAR,
  Contractor        CHAR,
  Job               CHAR,
  "By"              CHAR,
  Comments          CHAR,
  UserLogoChecked   Boolean not null,
  UserLogo          CHAR,
  ClientLogoChecked Boolean not null,
  ClientLogo        CHAR,
  WellLocation      CHAR,
  AirGap            CHAR,
  WaterDepth        float,
  SubseaWellheadChecked Boolean not null,
  "Index"           INT);''')

# Survey
c.execute('''
create table Survey
(
  ID    INTEGER PRIMARY KEY  AUTOINCREMENT   not null,
  BHA_ID            int not null
    constraint BHA_ID
    references BHAData,
  ClassType         int,
  AnnotationChecked Boolean,
  TortuosityChecked Boolean,
  ProjectAziChecked Boolean,
  ProjectAzi        CHAR,
  MaxTortuosity     CHAR,
  "Index"           int
); ''')

# SurveyRow
c.execute('''
create table SurveyRow
(
  ID    INTEGER PRIMARY KEY  AUTOINCREMENT   not null,
  SurveyID int  not null
    constraint SurveyID
    references Survey,
  BHA_ID   int not null
    constraint BHA_ID
    references BHAData,
  ClassType     CHAR,
  MD            CHAR,
  Inc           CHAR,
  Azi           CHAR,
  "Index"       int
);
''')

# AnnotationRow
c.execute('''
create table AnnotationRow
(
  ID    INTEGER PRIMARY KEY  AUTOINCREMENT   not null,
  SurveyID     int not null
    constraint SurveyID
    references Survey,
  ClassType    CHAR,
  MD           CHAR,
  Annotation   CHAR,
  Symbol       CHAR,
  "Index"      int
);''')


# TortuosityRow
c.execute('''
create table TortuosityRow
(
  ID    INTEGER PRIMARY KEY  AUTOINCREMENT   not null,
  SurveyID          int not null
    constraint SurveyID
    references Survey,
  ClassType         CHAR,
  "From"            CHAR,
  "To"              CHAR,
  Amplitude         CHAR,
  Period            CHAR,
  Interval          CHAR,
  "Index"           int
);''')

# CasedHole
c.execute('''
create table CasedHoleRow
(
  ID    INTEGER PRIMARY KEY  AUTOINCREMENT   not null,
  BHA_ID            int     not null
    constraint BHA_ID
    references BHAData,
  ClassType      CHAR,
  Bottom         CHAR,
  Description    CHAR,
  InnerDiameter  CHAR,
  FrictionFactor CHAR,
  "Index"        int
);''')

# OpenHoleRow
c.execute('''
create table OpenHoleRow
(
  ID    INTEGER PRIMARY KEY  AUTOINCREMENT   not null,
  BHA_ID            int     not null
    constraint BHA_ID
    references BHAData,
  ClassType      CHAR,
  Bottom         CHAR,
  Description    CHAR,
  InnerDiameter  CHAR,
  FrictionFactor CHAR,
  "Index"        int
);''')

# OperationRow
c.execute('''
create table OperationRow
(
  ID    INTEGER PRIMARY KEY  AUTOINCREMENT   not null,
  BHA_ID            int     not null
    constraint BHA_ID
    references BHAData,
  Description    CHAR,
  EndingDepth    CHAR,
  MW             CHAR,
  WOB            CHAR,
  TOB            CHAR,
  ROP            CHAR,
  RPM            CHAR,
  FrictionFactor CHAR,
  "Index"        int
);''')

# BHAComponentRow
c.execute('''
create table BHAComponentRow
(
  ID    INTEGER PRIMARY KEY  AUTOINCREMENT   not null,
  BHA_ID            int     not null
    constraint BHA_ID
    references BHAData,
  ClassType    CHAR,
  Description    CHAR,
  Type             CHAR,
  "Index"        int
);
''')

# BHAComponent
c.execute('''
create table BHAComponent
(
  ID    INTEGER PRIMARY KEY  AUTOINCREMENT   not null,
  BHA_ID            int     not null
    constraint BHA_ID
    references BHAData,
  ClassType    CHAR,
  Size    CHAR,
  Wt             CHAR,
  Length     CHAR,
  MakeupTorque CHAR
);
''')


print("Table created successfully")
conn.commit()
conn.close()

