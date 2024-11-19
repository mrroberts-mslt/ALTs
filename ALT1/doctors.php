<?php
// Database configuration
$servername = "localhost";
$username = "lccs_huw2";
$password = "YNbW8iHH8MKH";
$database = "lccs_huw";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Define the SQL query
$sql = "SELECT * FROM doctors";
$result = $conn->query($sql);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Output</title>
    <style>
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Data from MySQL Database</h1>
    <table>
        <thead>
            <tr>
                <?php
                // Output column headers
                if ($result->num_rows > 0) {
                    $row = $result->fetch_assoc();
                    foreach ($row as $column => $value) {
                        echo "<th>" . htmlspecialchars($column) . "</th>";
                    }
                    echo "</tr></thead><tbody>";

                    // Output the first row
                    echo "<tr>";
                    foreach ($row as $value) {
                        echo "<td>" . htmlspecialchars($value) . "</td>";
                    }
                    echo "</tr>";

                    // Output remaining rows
                    while ($row = $result->fetch_assoc()) {
                        echo "<tr>";
                        foreach ($row as $value) {
                            echo "<td>" . htmlspecialchars($value) . "</td>";
                        }
                        echo "</tr>";
                    }
                } else {
                    echo "<p>No data found.</p>";
                }
                ?>
            </tbody>
        </table>
    </body>
</html>

<?php
// Close the database connection
$conn->close();
?>
