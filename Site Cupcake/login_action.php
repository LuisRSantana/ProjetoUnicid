<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['name'];
    $email = $_POST['email'];
    $endereco = $_POST['address'];
    $telefone = $_POST['phone'];

    // Conectar ao banco de dados SQLite
    $db = new SQLite3('cupcake_app.db');
    
    // Inserir os dados do usuário na tabela
    $stmt = $db->prepare('INSERT INTO usuarios (nome, email, endereco, telefone) VALUES (:nome, :email, :endereco, :telefone)');
    $stmt->bindValue(':nome', $nome, SQLITE3_TEXT);
    $stmt->bindValue(':email', $email, SQLITE3_TEXT);
    $stmt->bindValue(':endereco', $endereco, SQLITE3_TEXT);
    $stmt->bindValue(':telefone', $telefone, SQLITE3_TEXT);
    $stmt->execute();

    // Redirecionar para uma página de sucesso ou login
    header('Location: sucesso.html');
    exit();
}
?>