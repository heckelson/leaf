<template>
  <div id="header" class="flex-row">
    <div class="navbar">
      <div class="navbar-container">
        <img
          src="../assets/tree_logo_transparent.png"
          alt=""
          class="logo_head"
        />
      </div>

      <div class="navbar-container" id="nav-elements">
        <a href="#">Map</a>
        <a href="#">Why?</a>
        <a href="#">Funding</a>
        <a href="#">About us</a>
        <a href="#">Impressum</a>
      </div>
    </div>

    <!--<div class="login-section">
            {% if 'username' in session %}
            <p>
                Logged in as user: {{ session['username'] }}
            </p>
            <p><a href="/auth/logout">Log out</a></p>
            {% else %}
            <div>
                <form action="/auth/login" method="POST">
                    <label>
                        Username
                        <input type="text" name="username" placeholder="Username">
                    </label>
                    <label>
                        Passwort
                        <input type="password" name="password" placeholder="Password">
                    </label>

                    <input type="submit" value="Log in">

                </form>


                {% endif %}
            </div>

        </div>-->
  </div>
</template>

<script></script>

<style scoped>
.logo_head {
  width: 40px;
  height: 40px;
  object-fit: cover;

  margin: 8px;
}

.navbar {
  min-height: 6vh;

  display: flex;
  flex-flow: row wrap;
  align-items: center;
  justify-content: center;

  font-family: "Montserrat", sans-serif;

  border-bottom: 2px solid #256eff;
}

.navbar-container {
  display: flex;
  flex-flow: row wrap;

  align-items: center;
  justify-content: center;
}

a {
  transition: transform 100ms;
  color: var(--grandeis-blue);
  text-decoration: none;

  margin: 8px;
}

a:hover {
  transform: translateY(-2px);
}
</style>
