<?php
$REQUIRE_CHAT_KEY = True; //Not done yet
$ANTI_TOXIC = True; //IF TRUE ENTER A API KEY ON LINE 5 https://support.perspectiveapi.com/s/docs-get-started?language=en_US
function analyzeToxicity($comment) {
    $ANTI_TOXIC_API_KEY = "AIzaSyAYyCnhTDYB4jiS_spoPxemfjDfVGluJjY";
    $MAX_TOXICITY = 0.5;
    $apiEndpoint = 'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze';
    $contentType = 'application/json';
    $requestPayload = array(
        'comment' => array(
            'text' => $comment
        ),
        'requestedAttributes' => array(
            'TOXICITY' => array(
                'scoreType' => 'PROBABILITY'
            )
        )
    );
    $jsonPayload = json_encode($requestPayload);
    $context = stream_context_create(array(
        'http' => array(
            'method' => 'POST',
            'header' => 'Content-Type: ' . $contentType . "\r\n"
                      . 'Content-Length: ' . strlen($jsonPayload) . "\r\n",
            'content' => $jsonPayload
        )
    ));
    $response = file_get_contents($apiEndpoint . '?key=' . $ANTI_TOXIC_API_KEY, false, $context);
    if ($response === FALSE) {
        echo("USER:  MESSAGE: SorryŁsomethingŁmessedŁupŁwhileŁcheckingŁyourŁmessage! TIME: ".time());
        exit;
    }
    $responseData = json_decode($response, true);
    $toxicityScore = $responseData['attributeScores']['TOXICITY']['summaryScore']['value'];
    if ($toxicityScore>$MAX_TOXICITY){
        $toxic = True;
    }
    else {
        $toxic = False;
    }
    return $toxic;
}

function topsekurtech($key, $data) { //Will i ever use this?
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
    if (strlen($_GET["msgl"]) > 100){
        die("Too long!");
    }
    if ($ANTI_TOXIC){
        if (analyzeToxicity($_GET["msgl"])){
            die("Your message was flaged as toxic!");
        }
    }
    
    echo $_GET["msgl"];
    array_push($lmaodb["username"],$lmaoedb[$debil][0]);
    array_push($lmaodb["message"],$kreten);
    array_push($lmaodb["time"],time());
    $myfile = fopen("db.json", "w");
    fwrite($myfile, json_encode($lmaodb));
}
}
?>