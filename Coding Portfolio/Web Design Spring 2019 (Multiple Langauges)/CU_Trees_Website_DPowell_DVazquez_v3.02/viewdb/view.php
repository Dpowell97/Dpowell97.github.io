
<!DOCTYPE html>

<html>

    <head>

        <!--
        File name: view.php
        Due Date: April 2019
        Last Edit: 03/30/19
        Authors: Dustin Powell
                 Daniel Vazquez

        Purpose: Select a table from the database to view. This page will show
                 up only if no table is currently viewed.

        Reference(s): https://www.w3schools.com/howto/howto_js_topnav.asp
                      https://www.w3schools.com/howto/howto_css_fixed_footer.asp
                      https://www.w3schools.com/css/ (syntax reference)
                      https://www.w3schools.com/html/ (syntax reference)
                      IT240 Course book (syntax reference)

        See readme.txt for change logs
        -->

        <!-- Website meta data to proivde a description, keywords, indexing of webpage,
             prohibiting robots, and prevents storing data within the cache.
        -->
        <meta name="Description" content="Webpage to view data inside of the Cumberland 
            University Tree Database" />

        <meta name="keywords" content="Cumberland, University, Tree, Database" />
     
        <meta name="robots" content="nofollow" />

        <meta http-equiv="pragma" content="no-cache" />

        <!-- Title of the website -->
        <title>Cumberland University Tree Database - View Database</title>
        
        <!-- CSS Styling -->
        <link rel="stylesheet" href="/css/cu_tree_db.css">

    </head>

    <!-- Website's header
         Reference: https://www.w3schools.com/php7/php7_include_require.asp
                    https://www.w3schools.com/howto/howto_js_topnav.asp       
    -->
    <?php
        include '../header-footer/header.html';
    ?>

    <!-- Webpage Content ----------------------------------------------------->
    <body>

        <!--Main body div to act as content place holder in body -->
        <div class="main_group">

            <!-- Used to show current webpage location -->
            <center><p class="website_welcome">View the Database</p></center>

            <!-- Contains elements to allow for table selection -->
            <div class="page_item">

                <?php
                    # Select the table options.
                    # Reference: https://www.w3schools.com/php7/php7_include_require.asp
                    include 'select.html';
                ?>
            </div>

            <!-- Additional Table Information -->
            <p class="page_item"> <b>Notice:</b> Blank fields listed in the table are fields
            that were unable to be determined from the estimates of the sample data collected.
            </p>

        </div>

    </body>

    <!-- Website's footer
         Reference: https://www.w3schools.com/php7/php7_include_require.asp
                    https://www.w3schools.com/howto/howto_css_fixed_footer.asp
    -->
    <?php
        include '../header-footer/footer.html';
    ?>

</html>
