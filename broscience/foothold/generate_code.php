<?php

function generate_activation_code($time) {
    $chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";

    srand($time);

    $activation_code = "";
    for ($i = 0; $i < 32; $i++) {
        $activation_code = $activation_code . $chars[rand(0, strlen($chars) - 1)];
    }
    return $activation_code;
}

$time = time();

for ($i = 0; $i < 200; $i++) {
    $res = generate_activation_code($time + $i);
    print($res . "\n");
}

for ($i = 200; $i >= 0; $i--) {
	$res = generate_activation_code($time - $i);
	print($res . "\n");
}
?>