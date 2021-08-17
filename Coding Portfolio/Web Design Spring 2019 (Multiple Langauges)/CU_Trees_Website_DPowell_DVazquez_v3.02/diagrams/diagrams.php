
<!DOCTYPE html>

<html>

    <head>

        <!--
        File Name: diagrams.php
        Due Date: April 2019
        Last Edit: 03/30/19
        Authors: Dustin Powell
                 Daniel Vazquez

        Purpose: Display the diagrams used to create the database.

        Reference(s): https://www.w3schools.com/howto/howto_js_topnav.asp
                      https://www.w3schools.com/howto/howto_css_fixed_footer.asp
                      https://www.w3schools.com/css/ (syntax reference)
                      https://www.w3schools.com/html/ (syntax reference)
                      IT240 Course book (syntax reference)

        See readme.txt for change logs
        -->
 
        <!-- Website meta data to proivde a description, keywords, indexing of webpage,
             prohibiting robots, and prevents storing data within the cache.
             Reference: IT240 course book
        -->
        <meta name="Description" content="Diagrams web page of the the Cumberland 
            University Tree Database display important figures of the project" />

        <meta name="keywords" content="Cumberland, University, Tree, Database, 
            E.R. Diagram" />
     
        <meta name="robots" content="nofollow" />

        <meta http-equiv="pragma" content="no-cache" />

        <!-- Title of the website -->
        <title>Cumberland University Tree Database - Diagrams</title>

        <!-- CSS Styling -->
        <link rel="stylesheet" href="../css/cu_tree_db.css">

    </head>

    <!-- Website's header
         Reference: https://www.w3schools.com/php7/php7_include_require.asp
                    https://www.w3schools.com/howto/howto_js_topnav.asp       
    -->
    <?php include '../header-footer/header.html';
    ?>

    <!-- Web page Content ---------------------------------------------------->
    <body>

        <!--Main body div to act as content place holder in body -->
        <div class="main_group">

            <!--
            The following displays decreased sized images on the page, while also
            making them links to display that very picture on a larger size
            for more detail.
            -->

            <div>

                <!-- Used to show current webpage location -->
                <center><p class="website_welcome">Database Project Diagrams</p></center>

                <!-- Image for E.R. diagram Header -->
                <center><h1 class="item_header">Database ER Diagram</h1></center>

                <!-- Description of Image for ER diagram -->
                <p class="page_item">Before the creation of the database, the class had
                to construct an entity-relationship diagram, ER digram for short, to show the 
                components needed within the database. A database consists of multiple parts with 
                on being called an entity type. The entity type within the ER diagram stores information
                such as a tree's location, species, measurements, identification, and the person that
                submitted the tree. Each entity has sub-components called attributes that is the data
                associated with the entity which is a tree. The attributes contain data such as a tree's
                age or identification number. The entities are stored in an entity type which has relationships 
                between other entity types to store data about a tree that is stored in the database. The 
                first version of the diagram consisted of three entity types and two relationships. The 
                final diagram contains five entity types and four relationships, which is shown below.
                <p>
                
                <!-- Image of E.R. diagram -->
                <a href = "/images/CU_Trees_ER_Diagram_v4.0.jpg">
                <img class="css_image" src = "/images/CU_Trees_ER_Diagram_v4.0.jpg"
                    alt = "Database Diagram" title = "E.R. Diagram: Click to enlarge" 
                    height = "250" width = "500" style = "margin:100x 100x;
                    display: block; margin-left: auto; margin-right: auto" /></a>

            </div>
           
            <br />

            <div>
                <!-- Image for campus grid Header -->
                <center><h1 class="item_header">Tree Location Reference Grid</h1></center>

                <!-- Description of Image for Campus Grid -->
                <p class="page_item"> The purpose of the location grid is to provide a estiamted
                area to locate the trees on campus. The grid is to be used in conjunction with GPS
                to speed up the process of relocating a tree. To create the grid an image from Google
                Earth was used to take an ariel photo of campus and then was imported into Google Draw
                to create the grid. The grid is three by four, the y-axis is labeled A through C, and
                the x-axis is labeled 1 through 4. The estimated area of each grid is 3.625 acres, with
                all grids together being a total estimated area of 43.36 acres. The sample set of data for
                testing the database was collected in grids B3 and B4. The grid is subject to change over
                time as the university changes the property, so the grid needs to be updated regularly.
                </p>

                <!-- Image for Campus Grid -->
                <a href = "/images/CU_Grid.jpg"><img class="css_image" src = "/images/CU_Grid.jpg" 
                    alt = "Campus Grid" title = "Cumberland University Grid: Click to enlarge"
                    height = "250" width = "500" style = "margin:100x 100x;
                    display: block; margin-left: auto; margin-right: auto" /></a>
            </div>

        <br /> 

        </div>
        
          

    </body>

    <!-- Website's footer
         Reference: https://www.w3schools.com/php7/php7_include_require.asp
                    https://www.w3schools.com/howto/howto_css_fixed_footer.asp
    -->
    <?php include '../header-footer/footer.html';
    ?>

</html>
