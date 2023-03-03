<?php
$REQUIRE_CHAT_KEY = True; //Not done yet
function topsekurtech($key, $data) { //Can be bypassed tbh but this aint supposed to be the most secure thing
    $result = "";
    for($a = 0, $b = 0; $a < strlen($data); $a++, $b++) {
        if($b >= strlen($key)) { $b = 0; }
        $result .= $data[$a] ^ $key[$b];
    }
    return $result;
}
//header('Content-type:application/json;charset=utf-8');
$count = 0;
if (isset($_GET["pswrd"]))
{
    $lmaodb = json_decode(file_get_contents("db.json"), true);
    if ($lmaodb["username"] == null) {
        echo("USER:  MESSAGE: ServerŁBootedŁUp! TIME: ".time());
    }
    foreach($lmaodb["username"] as $dba) {
        if ($dba != null){
        if ($count>0){
            echo("<br>");
        }
        echo("USER: ".$dba." MESSAGE: ".$lmaodb["message"][$count]." TIME: ".$lmaodb["time"][$count]);
        $count++;
        }
    }
}
if (isset($_GET["pswrde"]))
{
    $lmaodb = json_decode(file_get_contents("db.json"), true);
    $lmaoedb = json_decode(file_get_contents("users.json"), true);
    $debil = $_GET["userl"];
    $kreten = str_replace(" ","Ł",$_GET["msgl"]);
if (isset($lmaoedb[$debil])){
    array_push($lmaodb["username"],$lmaoedb[$debil][0]);
    array_push($lmaodb["message"],$kreten);
    array_push($lmaodb["time"],time());
    $myfile = fopen("db.json", "w");
    fwrite($myfile, json_encode($lmaodb));
}
}
?>