<?php

$grant_type = "authorization_code";
$client_id = "1000.AVXAOVCQJ5MT94809VNFYSR6Z0D294";
$client_secret = "e8500819ea1bdc33aa84812b10753fd1de5f0232fa";
$redirect_uri = "https://efactura.info";
$code = "Bearer 1000.58aaed7f9851a3f677394e4888b4e4e7.0c545e37ba64f1a02725986dd71bfd00";

$url = "https://accounts.zoho.com/oauth/v2/token?grant_type=" . $grant_type . "&client_id=" . $client_id . "&client_secret=" . $client_secret . "&redirect_uri=" . $redirect_uri . "&code=" . $code;

$curl = curl_init();

curl_setopt_array($curl, array(

    CURLOPT_URL => $url,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => "",
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "POST",
    CURLOPT_POSTFIELDS => "",
));

$response = curl_exec($curl);
$err = curl_error($curl);
curl_close($curl);

if ($err) {
    echo "cURL Error #:" . $err;
} else {
    echo $response;
}

?>