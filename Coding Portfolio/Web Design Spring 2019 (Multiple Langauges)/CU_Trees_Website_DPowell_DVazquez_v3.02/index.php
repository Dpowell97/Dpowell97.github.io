
<!DOCTYPE html>

<html>

    <head>
        
        <!--
        File name: index.php
        Due Date: April 2019
        Last Edit: 04/01/19
        Authors: Dustin Powell
                 Daniel Vazquez

        Purpose: Home page of the website.

        Reference(s): https://www.w3schools.com/howto/howto_js_topnav.asp
                      https://www.w3schools.com/howto/howto_css_fixed_footer.asp
                      https://www.w3schools.com/css/ (syntax reference)
                      https://www.w3schools.com/html/ (syntax reference)
                      IT240 Course book (syntax reference)

        See readme.txt for change logs
        -->
    
        <!-- Title of the website -->
        <title>Cumberland University Tree Database - Home</title>

        <!-- Website meta data to proivde a description, indexing of webpage,
             prohibiting robots, and prevents storing data within the cache.
             Reference: IT240 course book
        -->
        <meta name="Description" content="Home page of the the Cumberland 
            University Tree Database provding information about the project" />

        <meta name="keywords" content="Cumberland, University, Tree, Database" />
     
        <meta name="robots" content="nofollow" />

        <meta http-equiv="pragma" content="no-cache" /> 

        <!-- CSS Styling -->
        <link rel="stylesheet" href="css/cu_tree_db.css">

    </head>

    <!-- Website's header
         Reference: https://www.w3schools.com/php7/php7_include_require.asp
                    https://www.w3schools.com/howto/howto_js_topnav.asp
    -->
    <?php include 'header-footer/header.html'; ?>

    <!-- Webpage Content ----------------------------------------------------->
    <body>

        <!--Main body div to act as content place holder in body -->
        <div class="main_group">

            <!-- Welcome to website -->
            <center><p class="website_welcome">Welcome to the Cumberland 
            University Tree Database Website</p></center>

            <!--Page Topic Header -->
            <center><h1 class="item_header">Project Summary</h1></center>

            <!-- Summary of the project -->
            <p class="page_item">The Cumberland University Trees Database was created for 
            the university to keep an inventory of the trees located on the main university
            campus for research and educational purposes. The project was started during the
            Fall 2018 semester by the IT310 Databases course for students to obtain experience
            in using the MySQL database language. The database was completed during the course
            but was not open to public view due to not having a finished user interface to display
            the data. The project was later continued during the IT240 Web Design and Web Structures
            course by some of the students that completed to databases course to finally allow for
            public viewing.
            </p>

            <!-- Page Topic Header -->
            <center><h1 class="item_header">Photos</h1></center>

            <!--Project Photos -->
            <p class="page_item">The pictures below are photos of various trees around campus
            which were edited and taken by Dustin Powell and Daniel Vazquez</p>

            <!-- Slideshow of pictures 
                 Reference: https://www.w3schools.com/howto/howto_js_slideshow.asp -->
            <?php include 'slideshow.html'; ?>

             <!-- Page Topic Header -->
            <center><h1 class="item_header">The Database Construction Process</h1></center>

            <!-- List of database creation steps -->
            <ol class="page_item">

               <li><b>Determing a Data Set:</b>
               The first step of any database project is to determine a set of data. 
               Multiple sets of data exist on the Cumberland University campus that is suitable
               for creating a database. The class had to determine if the database was even needed
               for all the considered sets of data. The data set of trees on the main campus was
               selected due to time constraints and scale of the project compared to the other
               available data sets.
               </li>

               <br />

               <li><b>Database ER Diagram Creation:</b>
               The next step in creating the database was to construct an ER diagram which is 
               necessarily a blueprint of the database. The ER diagram provides a visual representation 
               of each component that is needed for the database to work. More information about the ER 
               diagram for this project can be located on the <a href="/diagrams/diagrams.php">Diagrams page</a>.
               </li>
               <br />

               <li><b>Defining Database Data Types:</b>
               For the database to work correctly, the data types have to be determined, 
               so the database knows how to handle and store the data. Each attribute is a 
               component of an entity, which is considered a tree and its information in this 
               project, that stores a part of the data of each entity entered into the database. 
               The attributes were coded with MySQL using the data types INT, CHAR, VARCHAR, DECIMAL, 
               and DATE.
               </li>

               <br />

               <li><b>Defining Database Constraints:</b>
               The next step is declaring the constraints within the database to further 
               help with handling data. Each attribute has its own set of constraints are
               guidelines for the stored data aside from its data type. The attribute Tnum,
               which is short for the tree number, is used to identify a tree and its related
               information. The same is done with Snum which is short for species number both
               of these numbers are called a key attribute or primary key. Some attributes can
               be null which means a null value is stored showing that no data is present. 
               The use of null is used for a tree's date of birth and death if the data cannot
               be determined. Almost all of the attribute must contain data, so they have a not
               null constraint.
               </li>

               <br />

               <li><b>Collect a Sample Data Set:</b>
               A sample set of data was collected to test the entire database once it enters
               into development to test for any needed modifications. A sample set of eight trees
               were collected on campus using algebra and trigonometry to make estimates. The data
               currently stored of the trees are liable to be changed since they are estimates used
               for testing and demonstration purposes. Approximate measurements and proper identification
               is needed before any formal inventorying or research is to be done using the database.
               </li>

               <br />

               <li><b>Campus Grid Created:</b>
               After collecting the data, a grid of the main university campus was created using
               Google Earth to capture an aerial photo of campus. The purpose of the grid is to make
               locating the trees easier. More information regarding the grid can be found on the
               <a href="/diagrams/diagrams.php">Diagrams page</a>.
               </li>

               <br />

               <li><b>Database Coding:</b>
               The MySQL Workbench was used to create the database on a MySQL server. The CREATE TABLE 
               query was used to define the entity type, attributes, data types, and constraints that exist
               with each entity type within the database based upon the ER diagram. Each entity type can also
               be referred to as a table in the database. Once all the tables and relationships are created,
               data can now be inserted for testing. The INSERT INTO query is used to add values into each 
               table doing so leads into the testing of the database for any errors that could occur.
               </li>

               <br />

               <li><b>Database Testing:</b>
               After the inital creation of the database and data is inserted. The database data types and
               constraints are changed and retested until the database works as planned.
               </li>

               <br />

               <li><b>Database Post-Development:</b>
               Once testing has concluded the database is considered complete. A backup of the database
               is created to counter any data loss issues which is conducted regularly. The database is 
               then also secured and prepared for public launch.
               </li>

            </ol>
         
            <!-- Spacer between content and page footer -->
            <br />

        </div>

    </body>

    <!-- Website's footer
         Reference: https://www.w3schools.com/php7/php7_include_require.asp
                    https://www.w3schools.com/howto/howto_css_fixed_footer.asp
    -->
    <?php include 'header-footer/footer.html'; ?>

</html>
