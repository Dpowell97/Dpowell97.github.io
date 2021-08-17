CREATE TABLE Tree
(
    Tnum            CHAR(9)      NOT NULL,
    Input_Date      DATE         NOT NULL,
    Lnum            INT          NOT NULL,
    Snum            INT          NOT NULL,
    PRIMARY KEY (Tnum),
);

CREATE TABLE Tree_Stats
(
    Tnum            CHAR(9)      NOT NULL,
    Age             INT          NOT NULL,
    DoB             DATE         NOT NULL,
    DoD             DATE,
    Height          INT          NOT NULL,
	DHB_no          INT          NOT NULL,
    PRIMARY KEY (Tnum),
);

CREATE TABLE Tree_Species
(
    Cname           VARCHAR(20)  NOT NULL,
    Snum            INT          NOT NULL,
    Family          VARCHAR(20)  NOT NULL,
    Genus           VARCHAR(20)  NOT NULL,
    Sepithet        VARCHAR(20)  NOT NULL,
    PRIMARY KEY (Snum),
);

CREATE TABLE Location
(
    Lnum            INT          NOT NULL,
    Gridnum         INT          NOT NULL,
    GPS             VARCHAR(20)  NOT NULL,
    PRIMARY KEY (Lnum),
);

CREATE TABLE Grid_Info
(
    CenterGPS       VARCHAR(20)  NOT NULL,
    Gridnum         INT          NOT NULL,
    Area            VARCHAR(4)   NOT NULL,
    PRIMARY KEY (Gridnum),
);

CREATE TABLE DB_User
(
    Fname           VARCHAR(10)  NOT NULL,
    Lname           VARCHAR(15)  NOT NULL,
    Tnum            CHAR(9)      NOT NULL,
    ID_No           INT          NOT NULL,
    PRIMARY KEY (Tnum),
);
    