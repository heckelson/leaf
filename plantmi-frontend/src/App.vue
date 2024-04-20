<template>
  <NavBarView />
  <MainContent />
</template>

<script>
import NavBarView from "./components/NavbarView.vue";
import MainContent from "./components/MainContent.vue";

export default {
  name: "App",
  components: {
    NavBarView,
    MainContent,
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  --pakistan-green: #243010;
  --tea-green: #c4d6b0;
  --golden-brown: #99621e;
  --grandeis-blue: #256eff;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;

  background-color: var(--tea-green);
  background-image: linear-gradient(to right, var(--tea-green), #b3b7c6);
  color: #000;

  /* for variable height header (flex) and map */
  display: flex;
  flex-direction: column;
  height: 100vh;
}
</style>
