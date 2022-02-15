<?php

$UserName = $_POST['UserName'];
$PassWord = $_POST['PassWord'];
$FirstName = $_POST['FirstName'];
$LastName = $_POST['LastName'];
$CompanyName = $_POST['CompanyName'];
$CompanyDetails = $_POST['CompanyDetails'];
$Email = $_POST['Email'];

$conn = new mysqli('localhost','root','','apparel_360');
if($conn->connect_error){
    die('Connection Failed : '.$conn->connect_error);
}else{
    $stmt = $conn->prepare("insert into signup(UserName,PassWord,FirstName,LastName,CompanyName, CompanyDetails,Email) 
                   values(?,?,?,?,?,?,?)");
    $stmt->bind_param("sssssss",$UserName,$PassWord,$FirstName,$LastName,$CompanyName,$CompanyDetails,$Email);
    $stmt->execute();
    echo "<script type='text/javascript'>alert('Successful');</script>";
    header("Location: HomePage.html");
    $stmt->close();
    $conn->close();
}
?>