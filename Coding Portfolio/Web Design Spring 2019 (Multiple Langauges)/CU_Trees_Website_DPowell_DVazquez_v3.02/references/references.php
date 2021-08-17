
<!DOCTYPE html>

<html>

    <head>
        <!--
        File name: references.php
        Due Date: April 2019
        Last Edit: 03/26/19
        Authors: Dustin Powell
                 Daniel Vazquez

        Purpose: List the references used to create the website.

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
        <meta name="Description" content="Webpage to display project references 
            of the Cumberland University Tree Database" />

        <meta name="keywords" content="Cumberland, University, Tree, Database" />
     
        <meta name="robots" content="nofollow" />

        <meta http-equiv="pragma" content="no-cache" />

        <!-- Title of the website -->
        <title>Cumberland University Tree Database - References</title>
        
        <!-- CSS Styling -->
        <link rel="stylesheet" href="/css/cu_tree_db.css">

    </head>

    <!-- Website's header
         Reference: https://www.w3schools.com/php7/php7_include_require.asp
                    https://www.w3schools.com/howto/howto_js_topnav.asp       
    -->
    <?php include '../header-footer/header.html'; ?>

    <!-- Webpage Content ----------------------------------------------------->
    <body>

        <!--Main body div to act as content place holder in body -->
        <div class="main_group">

            <!-- Used to show current webpage location -->
            <center><p class="website_welcome">Project References</p></center>

            <!-- Page Item Header -->
            <center><h1 class="item_header">List of References</h1></center>

            <!-- Descriping list of references -->
            <p class="page_item">The following sources were used in the creation of this site:</p>

            <ul class="page_item">
                <li><a href="https://www.w3schools.com/html/">W3Schools HTML Syntax Reference</a></li>

                <br />

                <li><a href="https://www.w3schools.com/css/">W3Schools CSS Syntax Reference</a></li>

                <br />

                <li><a href="https://www.w3schools.com/howto/howto_js_topnav.asp">W3Schools How-To Top Navigation</a></li>

                <br />

                <li><a href="https://www.w3schools.com/howto/howto_css_fixed_footer.asp">W3Schools Webpage Footer</a></li>

                <br />

                <li><a href="https://www.w3schools.com/php7/php7_include_require.asp">PHP7 Include Files</a></li>

                <br />

                <li><a href="https://stackoverflow.com/questions/29542576/how-do-i-get-the-value-of-a-radio-button-in-php">How to identify the
                     value of a radio button to be used in a different file</a></li>

                <br />

                <li><a href="https://www.w3schools.com/php/php_mysql_select.asp">PHP Select Data From MySQL</a></li>

                <br />

                <li><a href="https://www.w3schools.com/php/php_switch.asp">PHP 5 switch Statement</a></li>

                <br />

                <li><a href="http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm">MYSQL Commands</a></li>

                <br />

                <li><a href="https://stackoverflow.com/questions/813287/how-to-store-decimal-values-in-sql-server">Decimal values in SQL 
                     database</a></li>

                <br />

                <li><a href="https://www.w3schools.com/sql/sql_datatypes.asp">MYSQL Data Types</a></li>

                <br />

                <li><a href="https://stackoverflow.com/questions/11757537/css-image-size-how-to-fill-not-stretch">Stop images 
                     from stretching</a></li>

                <br />

                <li><a href="https://www.w3schools.com/howto/howto_css_image_center.asp">How TO - Center Images</a></li>

                <br />

            </ul>

        </div>

    </body>

     <!-- Website's footer
         Reference: https://www.w3schools.com/php7/php7_include_require.asp
                    https://www.w3schools.com/howto/howto_css_fixed_footer.asp
    -->
    <?php include '../header-footer/footer.html'; ?>

</html>
