
        Website: cutdb.com
       Due Date: April 2019
      Last edit: 04/01/2019
Current version: v3.02
        Authors: Daniel Vazquez
                 Dustin Powell

-------------------------------------------------------------------------------

Project: Create a website that displays a database of trees on Cumberland
         University campus.

-------------------------------------------------------------------------------

Honor Code: On my honor, I have neither given nor received unauthorized or 
            unacknowledged aid on this academic work and I am unaware of any
            violations of this code by others.

Signed: Dustin Powell
        Daniel Vazquez

-------------------------------------------------------------------------------

ATTENTION! - cutdb.com must be tested through an apache web server. Trying to
             test it by just opening the files will just create duplicates of
             the file being opened. This happens because the main files for the
             website are *.php. These files must be ran through a server to
             interpret the php first and then interpret the html in these
             files.

-------------------------------------------------------------------------------

Change log:

- v1.00 (02/19/2019)
    * First complete version of HTML & CSS. (dpowell)

- v1.01 (02/20/2019)
    * Modified header image so it does not overstretch. (dvazquez)
    * Fixed spacing of the links in the header bar. (dvazquez)
    * Removed the index.txt hyperlink on the header due to 
      redundancy. (dvazquez)

- v2.00 (03/06/2019)
    * Switched to php files for the following reasons: (dvazquez)
        1. Reference to just one header file instead of having the header
           hardcoded in everyfile for convenience purposes. (dvazquez)
        2. Easy and Straightforward connection to the trees 
           database. (dvazquez)
    * Complete restructure of the website directories. (dvazquez)
    * Database's tables are successuly displayed as html tables on the 
      website. (dvazquez)
    * Changed the size of the headings for every page. (dvazquez)
    * Added a brief description on each file about its purpose. (dvazquez)

- v2.01 (03/13/2019)
    * Included better documentation of the project in this readme.txt 
      file. (dvazquez)
    * Reverted to a version of the previous directory system. (dvazquez)

- v2.02 (03/16/2019)
    * Formated table for displaying tree information. (dpowell)
    * Cleaned up html layout for clarity. (dpowell)
    * Added a standard div for all pages to align content. (dpowell)
    * Added a footer file. (dpowell)

-v2.03 (03/20/2019)
    * Added external CSS file to the website (dpowell)
    * Moved most of the CSS to the CSS external file (dpowell)
    * Added Diagram information (dpowell)
    * Added explaination to tree tables about blank boxes (dpowell)
    * Applied CSS to subheaders within the page (dpowell)
    * Re-added which person conducted a change in readme.txt (dpowell)

-v3.00 (03/26/2019)
    * Fixed formatting issue with the website footer (dpowell)
    * Moved and added comments for all webpages (dpowell)
    * Added current webpage indicator text to all pages (dpowell)
    * Added information to footer (dvazquez)
    * Added more content to home page (dpowell)
    * Took pictures of trees around campus to put on website (dvazquez)
    * Background color change (dvazquez)

-v3.01
    * Updated and finalized all website content and footer (dpowell)
    * Moved the location of photos to before database creation 
      process. (dpowell)

-V3.02
    * Added a slideshow to show pictures. (dvazquez)

-------------------------------------------------------------------------------

To do:

- ???

-------------------------------------------------------------------------------

Acknowledgement Notes: The IT240 course book and the following links were use 
                       to use html, css, php, and apache web server. Also
                       listed are reasons for their use.

-> HTML Syntax Refernce:

     https://www.w3schools.com/html/

-> CSS Syntax Reference:

     https://www.w3schools.com/css/

-> PHP include function:

    https://www.w3schools.com/php7/php7_include_require.asp

-> How to identify the value of a radio button to be used in a different file:

    https://stackoverflow.com/questions/29542576/how-do-i-get-the-value-of-a-radio-button-in-php

-> PHP connection to the sql database:

    https://www.w3schools.com/php/php_mysql_select.asp

-> Switch statements in PHP:

    https://www.w3schools.com/php/php_switch.asp

-> MYSQL commands:

    http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm

-> Decimal values:

    https://stackoverflow.com/questions/813287/how-to-store-decimal-values-in-sql-server

-> MYSQL Data Types:

    https://www.w3schools.com/sql/sql_datatypes.asp

-> Stop images from stretching:

    https://stackoverflow.com/questions/11757537/css-image-size-how-to-fill-not-stretch

-> Table to display tree information:
    
    https://www.w3schools.com/css/css_table.asp

-> Website Header Information:
   
     https://www.w3schools.com/howto/howto_js_topnav.asp

-> Website Footer Information:

     https://www.w3schools.com/howto/howto_css_fixed_footer.asp

-------------------------------------------------------------------------------

Browsers used for Development:

    1. Google Chrome

Specs used for development:

    Computer 1:
        CPU: Inter Core i5-8250U @ 1.60GHz
        RAM: 8 GB
         OS: Ubuntu 18.04.2 LTS

    Computer 2:
        CPU: AMD A10-8700p
        RAM: 8 GB
         OS: Ubuntu 18.04.1 LTS

-------------------------------------------------------------------------------

File Structure:

    /
        -> index.php
        -> readme.txt
        -> slideshow.html
        diagrams
            -> diagrams.php
        header-footer
            -> header.html
            -> footer.html
        images
            -> CU_Grid.jpg
            -> CU_Trees_ER_Diagram_v4.0.jpg
            -> Campus.JPG
            -> Big_1.JPG
            -> Quad.JPG
            -> Tree1_1.JPG
            -> Tree2_1.JPG
            -> Tree3_1.JPG
            -> Tree4_1.JPG
            -> Vice_1.JPG
        references
            -> references.php
        viewdb
            -> select.html
            -> tables.php
            -> view.php
        css
            ->cu_tree_db.css

-------------------------------------------------------------------------------
