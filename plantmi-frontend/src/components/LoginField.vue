<template>
  <div class="navbar-container" id="login-field" ref="login_div">
    <form action="/auth/login" method="post">
      <div>
        <label
          >Username
          <input type="text" name="username" />
        </label>
      </div>
      <div>
        <label
          >Password
          <input type="password" name="password" />
        </label>
      </div>
      <div>
        <input type="submit" value="Log in" />
      </div>
    </form>
  </div>
</template>

<script>
export default {
  methods: {
    setVisibility: function (status) {
      if (status == true) {
        this.$refs.login_div.style["display"] = "inherit";
      } else {
        this.$refs.login_div.style["display"] = "none";
      }
    },
  },
};
</script>

<style scoped>
#login-field {
  display: none;
  /* TODO: change to 'none' once done with styling */

  margin: 8px;
  margin-top: 0;
}

#login-field input {
  margin: 8px;
}
</style>
