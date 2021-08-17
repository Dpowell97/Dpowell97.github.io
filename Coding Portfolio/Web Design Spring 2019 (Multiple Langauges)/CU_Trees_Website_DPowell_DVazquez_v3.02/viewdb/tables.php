
<!DOCTYPE html>

<html>

    <!-- Website's head -->
    <head>

        <!--
        File name: tables.php
        Due Date: April 2019
        Last Edit: 03/30/19
        Authors: Dustin Powell
                 Daniel Vazquez

        Purpose: Display the database's tables, depending on what was selected
                 with the radio buttons.

        Reference(s): https://www.w3schools.com/howto/howto_js_topnav.asp
                      https://www.w3schools.com/howto/howto_css_fixed_footer.asp
                      https://www.w3schools.com/css/css_table.asp
                      https://stackoverflow.com/questions/29542576/how-do-i-get-the-value-of-a-radio-button-in-php
                      https://www.w3schools.com/php/php_mysql_select.asp
                      https://www.w3schools.com/php/php_switch.asp
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
   
        <!-- CSS: Table Styling 
        Reference: https://www.w3schools.com/css/css_table.asp
        -->      
        <style>

            div table { border-collapse: collapse;
                        width: 100%;
                        border: 3px solid gray;
                      }
            div th { background-color: maroon;
                     color: white;
                   }  

            div th, td { text-align: center;
                         padding: 8px;
                       }

            div td { border: 1px solid gray;}

            div th { text-align: center; 
                     border-bottom: 3px solid gray;}

            div tr:nth-child(even){ background-color: #e5e5e5;}

            div tr:nth-child(odd){ background-color: white;}
        
           .tree_table { margin-left: 3cm;
                  margin-right: 3cm;
                  margin-top: 1cm;
                  margin-bottom: 1cm;
                  border: none;
                  overflow: scroll;
                }

        </style>

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
            <center><p class="website_welcome">View the Database</p></center>

            <!-- Contains elements to allow for table selection -->
            <div class="page_item">
                <?php include 'select.html'; ?>
            </div>

            <!-- Additional Table Information -->
            <p class="page_item"> <b>Notice:</b> Blank fields listed in the table are fields
            that were unable to be determined from the estimates of the sample data collected.
            </p>
             
            <div class="tree_table">
                <?php

# Reference: https://stackoverflow.com/questions/29542576/how-do-i-get-the-value-of-a-radio-button-in-php
# Used the reference on how to deal with the selection of the radio
# buttons in a different file.            
            if (isset($_POST['Submit'])) {
                $radioVal = $_POST['Tables'];
            }

# Reference: https://www.w3schools.com/php/php_mysql_select.asp
# Used to display the database in html tables.

            $servername = "localhost";
            $username = "root";
            $password = "password";
            $dbname = "CU_Trees_DB_v4.00";

            # Start connection
            $conn = new mysqli($servername, $username, $password, $dbname);
            # Check connection
            if ($conn-> connect_error) {
                die("Connection failed: ". $conn-> connect_error);
            }
            
            $sql = "SELECT * FROM $radioVal";
            $result = $conn->query($sql);

            if ($result->num_rows > 0) {
                echo "<table>";
                switch ($radioVal) {

# References: https://www.w3schools.com/php/php_switch.asp
# Displays html table of the corresponding database table depending on the value of $radioVal
                    case "Tree":
                        echo "<tr><th>Tree Number</th><th>Species Number</th><th>Input Date</th></tr>";
                        while ($row = $result-> fetch_assoc()) {
                            echo "<tr><td>". $row["Tnum"] ."</td><td>". $row["Snum"] ."</td><td>". $row["TDate"] ."</td></tr>";
                        }
                        break;

                    case "T_Info":
                        echo "<tr><th>Tree Number</th><th>Age</th><th>D.B.H.</th><th>Height</th><th>Date of Birth</th><th>Date of Death</th></tr>";
                        while ($row = $result-> fetch_assoc()) {
                            echo "<tr><td>". $row["TI_Tnum"] ."</td><td>". $row["IT_Age"] ."</td><td>". $row["TI_DBH"] ."</td><td>". $row["TI_Height"] ."</td><td>". $row["TI_DoB"] ."</td><td>". $row["TI_DoD"] ."</td></tr>";
                        }
                        break;

                    case "T_Location":
                        echo "<tr><th>Tree Number</th><th>GPS Latitude</th><th> GPS Longitude</th><th>Grid Number</th></tr>";
                        while ($row = $result-> fetch_assoc()) {
                            echo "<tr><td>". $row["TL_Tnum"] ."</td><td>". $row["TL_LAT"] ."</td><td>". $row["TL_LNG"] ."</td><td>". $row["TL_Gnum"] ."</td></tr>";
                        }
                        break;

                    case "T_User":
                        echo "<tr><th>Tree Number</th><th>ID Number</th><th>Last Name</th><th>First Name</th></tr>";
                        while ($row = $result-> fetch_assoc()) {
                            echo "<tr><td>". $row["TU_Tnum"] ."</td><td>". $row["TU_IDnum"] ."</td><td>". $row["TU_Lname"] ."</td><td>". $row["TU_Fname"] ."</td></tr>";
                        }
                        break;

                    case "T_Taxonomy":
                        echo "<tr><th>Species Number</th><th>TT_Cname</th><th>Family</th><th>Genus</th><th>Specific Epithet</th></tr>";
                        while ($row = $result-> fetch_assoc()) {
                            echo "<tr><td>". $row["TT_Snum"] ."</td><td>". $row["TT_Cname"] ."</td><td>". $row["TT_Family"] ."</td><td>". $row["TT_Genus"] ."</td><td>". $row["TT_Spe_Ep"]."</td></tr>";
                        }
                        break;
                }

            } else {
                echo "0 results";
            }

            echo "</table>";

            $conn-> close();        

                ?>
            </div>


        </div>

    </body>

    <!-- Website's footer
         Reference: https://www.w3schools.com/php7/php7_include_require.asp
                    https://www.w3schools.com/howto/howto_css_fixed_footer.asp
    -->

    <?php include "../header-footer/footer.html"; ?>
    
</html>
