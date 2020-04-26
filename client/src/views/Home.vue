<template>
  <v-row>
    <v-col cols="3">
      <Logo />
    </v-col>
    <v-col cols="6">
      <v-row>
        <Description />
      </v-row>
      <v-row>
        <Users />
      </v-row>
      <div class="py-12"></div>
    </v-col>
    <v-col cols="3"></v-col>
  </v-row>
</template>

<script>
import Logo from "../shared/Logo";
import Description from "../components/Description";
import Users from "../components/Users";
export default {
  components: { Logo, Description, Users },
  name: "Home",
};
</script>
