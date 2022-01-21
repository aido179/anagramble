<template>
  <div class="modal-container" v-show="show">
    <div class="underlay" @click="handleClose"></div>
    <div class="modal-content" >
      <div class="close-icon" @click="handleClose">
        <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24">
          <path fill="var(--color-tone-3)" d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
        </svg>
      </div>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  props: {
  },
  data: () => {
    return {
      show: true,
    }
  },
  methods: {
    handleClose () {
      this.show = false
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.modal-container {
  z-index: 9000;
  position:fixed;
  top:0;
  left: 0;
  width: 100%;
  height: 100%;
}
.modal-content {
  position:absolute;
  top: 50%;
  left:50%;
  transform: translate(-50%, -50%);
  min-width: 100px;
  min-height: 100px;
  background-color: #fcfcfc;
  border-radius: 4px;
  border: 1px solid #fafafa;
  box-shadow: 0px 5px 21px -4px rgba(0,0,0,0.5);
  padding: 20px;
  text-align: left;
}
.underlay {
  position:fixed;
  top:0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(1,1,1,0.2)
}
.close-icon{
  position: absolute;
  right: 10px;
  top:10px;
}
</style>
