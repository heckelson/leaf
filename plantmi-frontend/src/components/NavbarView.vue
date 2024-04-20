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

      <div class="navbar-container nav-elements" v-if="isUsernameCookieSet()">
        <a href="/auth/logout">({{ getUsernameFromCookie() }}) Logout</a>
      </div>

      <div class="navbar-container nav-elements" v-else>
        <a href="#" @click="toggleLoginVisible()">Login</a>
      </div>
    </div>

    <LoginField ref="login_field" />
  </div>
</template>

<script>
import { inject } from "vue";
import LoginField from "./LoginField.vue";

export default {
  setup: function () {},
  components: {
    LoginField,
  },
  data: function () {
    return {
      login_is_visible: false,
    };
  },
  methods: {
    toggleLoginVisible: function () {
      this.login_is_visible = !this.login_is_visible;
      this.$refs.login_field.setVisibility(this.login_is_visible);
    },
    isUsernameCookieSet: function () {
      const $cookies = inject("$cookies");
      return $cookies.isKey("username");
    },
    getUsernameFromCookie: function () {
      const $cookies = inject("$cookies");
      return $cookies.get("username");
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
</style>
