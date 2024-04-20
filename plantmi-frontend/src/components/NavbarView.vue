<template>
  <div id="header">
    <div class="navbar">
      <div class="navbar-container">
        <a href="#">
          <img
            src="../assets/tree_logo_transparent.png"
            alt=""
            class="logo_head"
          />
        </a>
      </div>

      <div class="navbar-container nav-elements">
        <a href="#">Map</a>
        <a href="#">Why?</a>
        <a href="#">Funding</a>
        <a href="#">About us</a>
        <a href="#">Impressum</a>
      </div>

      <!--
        TODO: Add v-if and v-else; if logged out show this, else show the username
          and a logout field.
      -->

      <div class="navbar-container nav-elements">
        <a href="#" @click="toggleLoginVisible()">Login</a>
      </div>
    </div>

    <div class="navbar-container" id="login-field" ref="login_field">
      <form action="/login" class="navbar-container">
        <div><label>Username</label><input type="text" /></div>
        <div><label>Password</label><input type="password" /></div>
        <div><button type="submit">Login</button></div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      login_is_visible: true, // TODO: change to false once done with styling
    };
  },
  methods: {
    toggleLoginVisible: function () {
      this.login_is_visible = !this.login_is_visible;

      if (this.login_is_visible) {
        this.$refs.login_field.style["display"] = "inherit";
      } else {
        this.$refs.login_field.style["display"] = "none";
      }
    },
  },
};
</script>

<style scoped>
.logo_head {
  width: 40px;
  height: 40px;

  margin: 8px;
}

#header {
  border-bottom: 2px solid #256eff;
  font-family: "Montserrat", sans-serif;
  font-weight: 500;
}

.navbar {
  min-height: 6vh;

  display: flex;
  flex-flow: row wrap;
  align-items: center;
  justify-content: space-between;
}

.navbar-container {
  align-self: center;

  display: flex;
  flex-flow: row wrap;
  align-items: center;
  justify-content: center;
}

.nav-elements a {
  color: var(--grandeis-blue);
  text-decoration: none;

  margin: 8px;

  transition: all 150ms;
}

.nav-elements a:hover {
  font-weight: 700;
  transform: translateY(-2px);
}

#login-field {
  display: inherit;
  /* TODO: change to 'none' once done with styling */

  margin: 8px;
  margin-top: 0;
}

#login-field input {
  margin: 8px;
}
</style>
