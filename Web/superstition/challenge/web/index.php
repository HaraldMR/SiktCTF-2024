<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Page Loader</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="message-box">
            <?php
            if (isset($_GET['page'])) {
                $page = $_GET['page'];

                // Remove any instances of ../
                $page = str_replace('../', '', $page);

                // Block absolute paths
                if (strpos($page, '/') === 0) {
                    echo "<div class='message'>Not allowed: " . htmlspecialchars($page) . "</div>";
                } else {
                    // Check if the file exists and include it, otherwise show an error message
                    if (file_exists($page)) {
                        echo "<div class='message'>Loading page: " . htmlspecialchars($page) . "</div>";
                        echo "</div>"; // Close the message-box div here
                        echo "<div class='content'>";
                        include($page);
                        echo "</div>"; // Close the content div
                    } else {
                        echo "<div class='message'>Page not found: " . htmlspecialchars($page) . "</div>";
                    }
                }
            } else {
                echo "<div class='message'>Welcome to the homepage!</div>";
            }
            ?>
        </div>
    </div>
</body>
</html>
