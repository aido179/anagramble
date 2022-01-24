<template>
  <div class="home">

    <div class="board-container" ref="board-container">
      <div>
          <h1>ANAGRAMBLE <small>Score: {{score}}</small></h1>
      </div>


      <modal>
        <p>Use the letters to make 3 words as long as you can.</p>
        <p>There is at least 1 word with 8 letters.</p>
        <p>Each word counts towards your score.</p>
        <p>After three guesses, the 8 letter word will be revealed.</p>

        <p><b>Scoring:</b> <br />
          3 or 4 letters: 1 point<br />
          5 letter: 2 points<br />
          6 letter: 3 points<br />
          7 letter: 5 points<br />
          8 letter: 8 points<br />
        </p>

        <p>A new anagram will be available each day!</p>
      </modal>

      <!-- shuffled letters / answer-->
      <div class="word-row" v-if="!showAnswer">
        <div class="word-tile blue-tile flip" :class="{squashed:squashShuffle, unsquashed:!squashShuffle, guessedLetter:shuffledGuessedLetters[idx]}" v-for="(letter, idx) in shuffled" v-bind:key="idx" :ref="'r0c'+idx">{{letter}}</div>
      </div>
      <div class="word-row" v-show="showAnswer">
        <div class="word-tile guessGreen flip" :class="{squashed:!unsquashAnswer, unsquashed:unsquashAnswer}" v-for="(letter, idx) in word" v-bind:key="idx" :ref="'r0c'+idx">{{letter}}</div>
      </div>
      <!-- guess 1 -->
      <div class="word-row" :class="{shakeRow:isShakingRow(0)}">
        <div class="word-tile" :class="{guessDisabled: currentGuessWord!=0, guessGreen:guesses0Col == 'green', guessBlue:isBlue(0, letter), shake:isShaking(0, idx)}" v-for="(letter, idx) in guesses0" v-bind:key="idx" :ref="'r0c'+idx">{{letter}}</div>
      </div>
      <!-- guess 2 -->
      <div class="word-row" :class="{shakeRow:isShakingRow(1)}">
        <div class="word-tile" :class="{guessDisabled: currentGuessWord!=1, guessGreen:guesses1Col == 'green', guessBlue:isBlue(1, letter), shake:isShaking(1, idx)}" v-for="(letter, idx) in guesses1" v-bind:key="idx" :ref="'r0c'+idx">{{letter}}</div>
      </div>
      <!-- guess 3 -->
      <div class="word-row" :class="{shakeRow:isShakingRow(2)}">
        <div class="word-tile" :class="{guessDisabled: currentGuessWord!=2, guessGreen:guesses2Col == 'green', guessBlue:isBlue(2, letter), shake:isShaking(2, idx)}" v-for="(letter, idx) in guesses2" v-bind:key="idx" :ref="'r0c'+idx">{{letter}}</div>
      </div>



      <div class="not-a-word-message" :class="{hiddenTile: !showMessage, fade: showMessage}">
        <span>{{messageText}}</span>
      </div>

      <div class="keyboard">
        <div class="keyboard-row">
          <button class="keyboard-tile" @click="handleKeyboardKey">q</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">w</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">e</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">r</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">t</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">y</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">u</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">i</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">o</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">p</button>
        </div>
        <div class="keyboard-row">
          <div class="spacer half"></div>
          <button class="keyboard-tile" @click="handleKeyboardKey">a</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">s</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">d</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">f</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">g</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">h</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">j</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">k</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">l</button>
          <div class="spacer half"></div>
        </div>
        <div class="keyboard-row">
          <button class="keyboard-tile one-and-a-half" @click="handleEnter">ENTER</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">z</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">x</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">c</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">v</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">b</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">n</button>
          <button class="keyboard-tile" @click="handleKeyboardKey">m</button>
          <button class="keyboard-tile one-and-a-half" @click="handleBackspace">
            <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24">
                <path fill="var(--color-tone-1)" d="M22 3H7c-.69 0-1.23.35-1.59.88L0 12l5.41 8.11c.36.53.9.89 1.59.89h15c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H7.07L2.4 12l4.66-7H22v14zm-11.59-2L14 13.41 17.59 17 19 15.59 15.41 12 19 8.41 17.59 7 14 10.59 10.41 7 9 8.41 12.59 12 9 15.59z"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/*
TODO:
- pre-shuffle words so everybody gets the same shuffle
- pick one word per day
- generate emoji output
🟩🟩🟩🟩🟩🟩🟩🟩  If a valid 8 letter word (10 pts)
🟦🟦🟦🟦🟦⬜⬜⬜  5 letter word
🟦🟦🟦🟦⬜⬜⬜⬜  4 letter word
🟦🟦🟦⬜⬜⬜⬜⬜  4 letter word
*/
// @ is an alias to /src
// import _5words from '@/assets/5LetterWords.js'
import _8words from '@/assets/8LetterWords.js'
import modal from '@/components/modal.vue'
var wordLists = {}
export default {
  name: 'Home',
  components: {
    modal
  },
  data: () => {
    return {
      word: 'testword',
      wordLetterCounts: {},
      guessLetterCounts: {},
      shuffled: 'shuffled',
      shuffledGuessedLetters: [], // arr of bools for each char in shuffled if it has been guessed.
      guesses0: '        ',
      guesses1: '        ',
      guesses2: '        ',
      guesses0Col: 'none',
      guesses1Col: 'none',
      guesses2Col: 'none',
      guessInput: "",
      guessesEntered: [],
      currentGuessWord: 0,
      currentGuessLetter: 0,
      shake: false,
      shakeRow: false,
      showMessage: false,
      messageText: "",
      score: 0,

      showAnswer: false,
      squashShuffle: false,
      unsquashAnswer: false,
    }
  },
  created: function () {
    let wordIndex = Math.floor(_8words.words.length*Math.random());
    this.word = _8words.words[wordIndex]
    this.shuffled = this.word.split("").sort(() => 0.5 - Math.random());
    this.wordLetterCounts = this.countLetters(this.word)
    document.addEventListener("keydown", (event) => {
      let letters = "abcdefghijklmnopqrstuvwxyz"
      if (letters.includes(event.key)){
        this.handleLetterGuess(event.key)
      }
      if (event.key == "Backspace") {
        this.handleBackspace()
      }
      if (event.key == "Enter") {
        this.handleEnter()
      }
    });
  },
  mounted: async function () {
    /*
      Dynamically load the full word lists so I dont have to type out the whole thing...
    */
    let letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for (const letter of letters.split("")) {
      import(`@/assets/allwords/${letter}words.js`)
        .then((module) => {
          wordLists[letter] = module.default.words
        });
    }
  },
  methods: {
    countLetters: function (word) {
       // count occurances of each letter for validation
      return [...word].reduce((prev, curr) => { prev[curr] = prev[curr] ? prev[curr] + 1 : 1; return prev }, {});
    },
    handleKeyboardKey: function (event) {
      this.handleLetterGuess(event.target.innerText)
    },
    handleLetterGuess: function (letter) {
      letter = letter.toLowerCase()
      if (this.guessInput.length < 8) {
        if (this.word.split("").includes(letter) && (this.guessLetterCounts[letter] || 0) < this.wordLetterCounts[letter]) {
          this.guessInput = this.guessInput + letter
          this['guesses'+this.currentGuessWord] = (this.guessInput+ "        ").slice(0,8)
          this.guessLetterCounts = this.countLetters(this.guessInput)
          this.shuffledGuessedLetters = this.identifyGuessedLetters()
        } else {
          // don't allow letter to be entered.
          this.shake = true
          setTimeout(() => {
            this.shake = false
          }, 1000)
        }
      }
    },
    handleBackspace: function () {
      if (this.guessInput.length > 0) {
        this.guessInput = this.guessInput.slice(0,-1)
        this['guesses'+this.currentGuessWord] = (this.guessInput+ "        ").slice(0,8)
        this.guessLetterCounts = this.countLetters(this.guessInput)
        this.shuffledGuessedLetters = this.identifyGuessedLetters()
      }
    },
    handleEnter: function () {
      if (this.currentGuessWord < 3 && this.guessInput.length > 0) {
        let letter1 = this.guessInput.toUpperCase().split("")[0]
        if (this.guessesEntered.includes(this.guessInput)) {
          this.handleShowMessage("Word already entered.")
          return
        }
        if (wordLists[letter1].includes(this.guessInput)) {
          // is a real word
          this.guessesEntered.push(this.guessInput)
          if (this.guessInput == this.word) {
            this[`guesses${this.currentGuessWord}Col`] = "green"
          } else if (true) {
            this[`guesses${this.currentGuessWord}Col`] = "blue"
          }
          if (this.guessInput.length >= 3 && this.guessInput.length <= 4) this.score += 1
          if (this.guessInput.length == 5) this.score += 2
          if (this.guessInput.length == 6) this.score += 3
          if (this.guessInput.length == 7) this.score += 5
          if (this.guessInput.length == 8) this.score += 8
          this.currentGuessWord+=1
          this.guessInput = ""
          this.guessLetterCounts = this.countLetters(this.guessInput)
          if (this.currentGuessWord == 3) {
            this.handleShowAnswer()
          }
        } else {
          // not a real word
          this.shakeRow = true
          setTimeout(() => {
            this.shakeRow = false
          }, 1000)
          this.handleShowMessage("Not in word list.")
        }
      }
    },
    handleShowMessage: function (messageText) {
      this.messageText = messageText
      this.showMessage = true
      setTimeout(() => {
        this.showMessage = false
        this.messageText = ""
      }, 3000)
    },
    identifyGuessedLetters: function (letter, index) {
      let inputcpy = `${this.guessInput}` // copy of input
      let lettersToCheck = [...this.shuffled].join("")
      let shuffledIsGuessed = this.shuffled.map((letter) => {
        if (inputcpy.includes(letter)) {
          inputcpy = inputcpy.replace(letter, '')
          return true
        }
        return false
      })
      return shuffledIsGuessed
    },
    isBlue: function (wordIndex, letter) {
      return (this[`guesses${wordIndex}Col`] == 'blue' && letter != " ")
    },
    isShaking: function (wordIndex, letterIndex) {
      return (this.shake && wordIndex == this.currentGuessWord && letterIndex == this.guessInput.length)
    },
    isShakingRow: function (wordIndex) {
      return (this.shakeRow && wordIndex == this.currentGuessWord)
    },
    handleShowAnswer: function () {
      this.squashShuffle = true
      setTimeout(() => {
        this.showAnswer = true
        setTimeout(() => {
          this.unsquashAnswer = true
        }, 200)
      }, 800)
    }
  },
};
</script>

<style>
html {
  font-family: 'Clear Sans', 'Helvetica Neue', Arial, sans-serif;
}
h1 {
  text-align: left;
  padding: 0 6px;
}
small {
  float: right;
}
.board-container {
  box-sizing: border-box;
  position:relative;
  display:flex;
  width: 500px;
  height: 675px;
  margin: 0 auto;
  /* border: 4px solid black; */
  flex-direction: column;
  align-items: stretch;
  align-content: stretch;
  overflow: hidden;
}
.not-a-word-message{
  position: absolute;
  top: 150px;
  left: 50%;
  transform: translate(-50%);
  background-color: #787c7e;
  color: #ffffff;
  font-family: inherit;
  font-weight: bold;
  border-radius: 6px;
  padding: 15px;
}
.word-row {
  width: 100%;
  height: 62px;
  margin-bottom: 12px;
  display: flex;
  justify-content: center;
  align-content: stretch;
}
.word-tile{
  flex: 1 100%;
  height: 62px;
  margin: 6px;
  border: 2px solid rgb(86, 87, 88);
  font-size: 32px;
  font-weight: 700;
  line-height: 62px;
  text-transform: uppercase;
}
.blue-tile {
  background-color: #43609f; /*#294580;*/
  color: #ffffff;
  border: None;
}
.guessDisabled{
  border: 2px solid rgba(86, 87, 88, 0.1);
}
.guessGreen {
  background-color: #6aaa64; /*#294580;*/
  color: #ffffff;
  border: 2px solid rgba(86, 87, 88, 0.1);
}
.guessBlue {
  background-color: #748cc1; /*#294580;*/
  color: #ffffff;
  border: 2px solid rgba(86, 87, 88, 0.1);
}
.guessedLetter{
  background-color: #a6b7db;
}
.hiddenTile {
  background-color: rgba(0,0,0,0); /*#294580;*/
  color: rgba(0,0,0,0);
  border: None;
}
.score {
  display: flex;
}
.keyboard{
  width: 100%;
  position: absolute;
  bottom: 0;
}
.keyboard-row{
  width: 100%;
  height: 62px;
  margin-bottom: 12px;
  display: flex;
  justify-content: center;
  align-content: stretch;
}
.keyboard-tile{
  font-family: inherit;
  font-weight: bold;
  border: 0;
  padding: 0;
  margin: 0 3px 0 3px;
  height: 58px;
  border-radius: 4px;
  cursor: pointer;
  user-select: none;
  background-color: #d3d6da;
  color: #1a1a1b;
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  text-transform: uppercase;
  -webkit-tap-highlight-color: rgba(0,0,0,0.3);
}
.keyboard-tile:active{
  background-color: #878a8c;
}
.half {
    flex: 0.5;
}
.one-and-a-half {
    flex: 1.5;
    font-size: 12px;
}
.shake {
  animation: shake 0.82s cubic-bezier(.36,.07,.19,.97) both, red 0.82s cubic-bezier(.36,.07,.19,.97) both;
  transform: translate3d(0, 0, 0);
}
.shakeRow {
  animation: shake 0.82s cubic-bezier(.36,.07,.19,.97) both;
  transform: translate3d(0, 0, 0);
}
.fade {
  animation: fade 3s cubic-bezier(.36,.07,.19,.97) both;
}
.flip {
  perspective: 1000px;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}
.squashed {
  transform: rotateY(90deg);
}
.unsquashed {
  transform: rotateY(0deg);
}
@keyframes shake {
  10%, 90% {
    transform: translate3d(-1px, 0, 0);
  }
  20%, 80% {
    transform: translate3d(2px, 0, 0);
  }
  30%, 50%, 70% {
    transform: translate3d(-4px, 0, 0);
  }
  40%, 60% {
    transform: translate3d(4px, 0, 0);
  }
  100% {
    background-color: #ffffff;
  }
}
@keyframes red {
  0% {
    background-color: #dd5050;
  }
  100% {
    background-color: #ffffff;
  }
}
@keyframes fade {
  0% {
    opacity: 1;
  }
  100% {
      opacity: 0;
  }
}


</style>
