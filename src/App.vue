<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <router-view/>
  </div>
</template>

<style>
body {
  margin:0;
  padding:0;
}
/* Global Styles & Colors */
:root {
  --red: #dd5050;

  --green: #6aaa64;
  --darkendGreen: #538d4e;
  --yellow: #c9b458;
  --darkendYellow: #b59f3b;
  --lightGray: #d8d8d8;
  --gray: #86888a;
  --darkGray: #939598;
  --white: #fff;
  --black: #212121;
  /* Colorblind colors */
  --orange: #f5793a;
  --blue: #85c0f9;
  font-family: 'Clear Sans', 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  --header-height: 50px;
  --keyboard-height: 200px;
  --game-max-width: 500px;
}
/* Light theme colors */
.light-theme {
  --color-tone-1: #1a1a1b;
  --color-tone-2: #787c7e;
  --color-tone-3: #878a8c;
  --color-tone-4: #d3d6da;
  --color-tone-5: #edeff1;
  --color-tone-6: #f6f7f8;
  --color-tone-7: #ffffff;
  --opacity-50: rgba(255, 255, 255, 0.5);

}
.dark-theme {
  --color-tone-1: #d7dadc;
  --color-tone-2: #818384;
  --color-tone-3: #565758;
  --color-tone-4: #3a3a3c;
  --color-tone-5: #272729;
  --color-tone-6: #1a1a1b;
  --color-tone-7: #121213;
  --opacity-50: rgba(0, 0, 0, 0.5);


}
/*Dark Theme Colors */
 /* @media (prefers-color-scheme: dark) {
  :root {
    --color-tone-1: #d7dadc;
    --color-tone-2: #818384;
    --color-tone-3: #565758;
    --color-tone-4: #3a3a3c;
    --color-tone-5: #272729;
    --color-tone-6: #1a1a1b;
    --color-tone-7: #121213;
    --opacity-50: rgba(0, 0, 0, 0.5);
  }
  .light-theme {
    --color-tone-1: #1a1a1b;
    --color-tone-2: #787c7e;
    --color-tone-3: #878a8c;
    --color-tone-4: #d3d6da;
    --color-tone-5: #edeff1;
    --color-tone-6: #f6f7f8;
    --color-tone-7: #ffffff;
    --opacity-50: rgba(255, 255, 255, 0.5);
  }
} */

/* Constant colors and colors derived from theme */
.theme, .theme > *{
  --text-color: var(--color-tone-1);
  --color-background: var(--color-tone-7);

  color: var(--text-color);
  background-color: var(--color-background);

  --tile-text-color: #ffffff;
  --tile-blue: #43609f;
  --tile-blue-light: #748cc1;

  --color-disabled: var(--color-tone-5);
  --color-active: var(--color-tone-3);

  --key-text-color: var(--color-tone-1);
  --key-bg: var(--color-tone-4);
  --key-active-bg: var(--color-tone-5);
  --modal-content-bg: var(--color-tone-7);
  --modal-content-border: var(--color-tone-6);
}

.theme.light-theme {

}

.colorblind {
  --color-correct: var(--orange);
  --color-present: var(--blue);
  --tile-text-color: var(--white);
  --key-bg-present: var(--color-present);
  --key-bg-correct: var(--color-correct);
  --key-bg-absent: var(--color-absent);
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
