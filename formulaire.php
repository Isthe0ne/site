<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amazon sign in</title>
    <link rel="stylesheet" href="formulaire.css">
</head>

<body>
    <div class="login-container">

	<div class="amazon-logo">
            <img src="/img/logo.webp" alt="Amazon Logo">
        </div>

	<div class="login-box">
            <h1>Sign-In</h1>
            <form action="#" method="POST">
                <label for="email">Email or mobile phone number</label>
                <input type="text" id="email" name="email" required>
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
                <a href="#">Forgot your password?</a>
                <button type="submit">Sign-In</button>
            </form>
        </div>

	<div class="create-account">
            <p>New to Amazon?</p>
            <a href="#">Create your Amazon account</a>
	</div>

    </div>
</body>
