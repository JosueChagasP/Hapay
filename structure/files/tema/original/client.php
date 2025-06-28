<?php
// Função para gerar uma string aleatória
function generateRandomString($length = 25) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, strlen($characters) - 1)];
    }
    return $randomString;
}

// Geração de chave de sessão
$randomPart = generateRandomString(10); // Parte aleatória da chave
$timePart = time(); // Parte baseada no tempo atual
$sessionKey = 'BR-' . $randomPart . $timePart . '-SSO'; // Combinação de partes

// Atualização do auth_ticket no banco de dados
$updateQuery = "UPDATE users SET auth_ticket='" . $sessionKey . "' WHERE username='" . usuario . "'";
$conn->query($updateQuery);

// Consulta para recuperar informações do usuário
$selectQuery = "SELECT * FROM users WHERE username='" . usuario . "'";
$queryResult = mysqli_query($conn, $selectQuery) or die(mysqli_error($conn));

// Processamento dos dados do usuário
if ($row = $queryResult->fetch_assoc()) {
    $idHabbozinho = $row['id'];
   // $verificado = $row['codigo'];
    $nominhoHabbo = $row['username'];
    //$estaVerificado = $row['verificado'];
    $m = $row['motto'];
    $rankstaff = $row['rank'];
    $fds = $row['auth_ticket'];
    $discordAtivado = 1;
}

// Configuração do cabeçalho para garantir a codificação correta
header('Content-Type: text/html; charset=utf-8');
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" crossorigin="use-credentials" href="/site.webmanifest">
    <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#000000">
    <meta name="apple-mobile-web-app-title" content="Nitro">
    <meta name="application-name" content="Nitro">
    <meta name="msapplication-TileColor" content="#000000">
    <meta name="theme-color" content="#000000" />
    <meta name="apple-mobile-web-app-capable" content="yes">
   
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <base href="./">
    <title>Client: {hotelname}</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="//comprahabbo.com/api/js/yt.js"></script>
   <script type="module" crossorigin src="http://localhost/nitro/assets/index-34d8c395.js?"></script>
<link rel="modulepreload" crossorigin href="http://localhost/nitro/assets/vendor-48792d42.js?">
<link rel="modulepreload" crossorigin href="http://localhost/nitro/assets/nitro-renderer-493a6bde.js?">
<link rel="stylesheet" href="http://localhost/nitro/assets/index.css?">

    <link rel="stylesheet" href="//comprahabbo.com/api/css/yt.css?">
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root" class="w-100 h-100"></div>
    <script>
      const NitroConfig = {
        "config.urls": [ 'http://localhost/renderer-config.json?<?php echo time() ?>', 'http://localhost/ui-config.json?<?php echo time() ?>' ],
        "sso.ticket": "<?= $sessionKey; ?>",
        "forward.type": (new URLSearchParams(window.location.search).get('room') ? 2 : -1),
        "forward.id": (new URLSearchParams(window.location.search).get('room') || 0),
        "friend.id": (new URLSearchParams(window.location.search).get('friend') || 0),
      };
    </script>


     

 <script src="//cdn.comprahabbo.com/structure//files/tema/original/game/push.js"></script>
  </body>
</html>
