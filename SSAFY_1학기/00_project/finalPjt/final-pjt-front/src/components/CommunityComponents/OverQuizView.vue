<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-3 d-flex align-items-center">
        <div class="col static">
          
          <h1>유저 랭킹!!</h1>
          <div class="profile-card" v-if="rankUser?.length == 0">
            <a href="#" class="text-white fs-6">아직 등록된 랭커가 없습니다. <br>가장 먼저 등록해보세요!</a>
          </div>
          <div class="profile-card" v-if="rankUser?.length">
            <img v-if="rankUser[0]?.image_base64" :src="getImageSrc(rankUser[0]?.image_base64)" alt="user" class="profile-photo">
            <img v-else src="../../assets/baseProfile.png" alt="user" class="profile-photo">
            <h3>1등</h3>
            <a href="#" class="text-white fs-6"><i class="fa-solid fa-crown fa-beat" style="color: #fff700;"></i> {{rankUser[0]?.overview_points}} 점 | {{rankUser[0]?.username}}</a>
          </div>

          <ul class="nav-news-feed" v-if="rank2users">
            <RankUserListView v-for="(user, index) in rank2users" :key="index"
              :user="user"
              :index="index"
              :quiztype="'over'"/>
          </ul>

        </div>
      </div>

      <div class="col-lg-9">
        <div class="card">
          <div class="card-body">
            <h2 class="card-title text-center fw-bold">줄거리 퀴즈</h2> 
            <div>현재 {{user?.username}}님의 최고 점수는 : {{user?.overview_points ? user?.overview_points : 0}}점 입니다.</div>
            <hr>
            <div class="d-flex justify-content-center">
              <div class="col-4 form-group d-flex justify-content-start align-item-center">

                <label for="genreSelect" class="col-3 fw-bold fs-5" style="width:100px">장르 선택:</label>
                <b-form-select v-model="genreSelected" :options="genereOptions" class="form-select" @change="filteredMovies"></b-form-select>

              </div>
              <button class="btn btn-danger ms-4 px-5" @click="gameStart">start</button>
            </div>

            <div class="text-center mb-4 text-white">

              <img src="../../assets/blackboard.png" alt="chalkboard" class="img-fluid">
              <div v-if="showStart" class="start-text">{{ startText }}</div>
              <div v-if="showCountdown === 3" class="countdown-text">{{ countdown }}</div>
              <div v-if="showCountdown === 2" class="countdown-text">{{ countdown }}</div>
              <div v-if="showCountdown === 1" class="countdown-text">{{ countdown }}</div>


              <div v-if="showCountdown === 0" class="quiz-text"> 

                <h4 v-if="!gameOver">장르: {{selectedGenreTitle}}</h4>

                <div v-if="!gameOver" class="fs-6">
                  문제 : {{ truncatedOverview }}

                  <span v-if="showFullOverview" class="text-info text-decoration-underline" style="cursor: pointer; " @click="toggleFullOverview">접기</span>
                  <span v-else class="text-info text-decoration-underline pointer" style="cursor: pointer;" @click="toggleFullOverview">더보기</span>  
                </div>

                <div v-if="gameOver" class="game-over-text">GAME OVER</div>

                <div class="answer-card-container" v-if="cardShow">
                  <div class="answer-card" :class="{ 'flipped': isFlipped }" @mouseenter="flipCard(true)" @mouseleave="flipCard(false)">
                    <div class="front">
                      <h3 style="color: red;">GAME OVER</h3>
                      <img :src="imgSrc" class="w-100 img-height" alt="img25">
                    </div>
                    <div class="back">
                      <button @click="closeCard">확인</button>
                    </div>
                  </div>
                </div>

              </div>

              <div v-if="showCountdown === 0" class="timer">{{ timer }}</div>

              <div v-if="showCountdown === 0" class="score-text">
                <p class="mb-1">맞춘 갯수: {{ answerCount}}</p>
                <p>현재 점수: {{ score }}</p>
              </div>
            </div>

            <div class="text-center d-flex justify-content-center">
              <h4 class="card-subtitle mb-4">정답: </h4>
              <input type="text" v-model="myAnswer" class="form-control" @keyup.enter="submitAnswer">
              <button class="btn btn-primary mt-3" @click="submitAnswer">확인</button> 
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import RankUserListView from './RankUserListView.vue'

export default {
  name: 'OverQuizView',
  components: {
    RankUserListView
  },
  data() {
    return {
      user: null,
      rankUser: null,

      genreSelected: 0,

      genereOptions: [
        { value: 0, text: '전체' },
        { value: 28, text: '액션' },
        { value: 12, text: '모험' },
        { value: 16, text: '애니메이션' },
        { value: 35, text: '코미디' },
        { value: 80, text: '범죄' },
        { value: 99, text: '다큐멘터리' },
        { value: 10751, text: '가족' },
        { value: 14, text: '판타지' },
        { value: 36, text: '역사' },
        { value: 27, text: '공포' },
        { value: 10402, text: '음악' },
        { value: 9648, text: '미스터리' },
        { value: 10749, text: '로맨스' },
        { value: 878, text: 'SF' },
        { value: 10770, text: 'TV 영화' },
        { value: 53, text: '스릴러' },
        { value: 10752, text: '전쟁' },
        { value: 37, text: '서부' },
      ],
      quizMovies: [],

      showStart: false,
      showCountdown: -1,
      startText: 'START',
      countdown: '',

      showFullOverview: false,
      
      currentQuiz: null,
      usedQuizIndexes: [],

      startCheck: false,
      myAnswer: "",
      timer: 10, // 초기 10초값
      timerInterval: null, 
      gameOver: false,
      score: 0,
      answerCount: 0,

      isFlipped: false,
      cardShow: false,
      imgSrc: "",
    }
  },
  methods: {
    
    // 선택된 장르에 따른 영화 가져오기
    filteredMovies() {
      if (this.genreSelected === 0) {
        this.quizMovies = this.$store.state.allmovie;
      } else {
        this.quizMovies = this.$store.state.allmovie.filter(movie => movie.genre_ids.includes(this.genreSelected));
      }

      // 영문으로만 되어 있는 제목을 걸러내기 위해 한번더 필터링 한다.
      let regex = /[ㄱ-ㅎㅏ-ㅣ가-힣]/;
      this.quizMovies = this.quizMovies.filter(movie => regex.test(movie.title));

    },

    // 랜덤 문제 출제
    pickRandomMovie() {
      const quizMovies = this.quizMovies;

      if (quizMovies.length === 0) {
        console.log('해당 장르 영화 정보가 없네요... 다른 장르 할래요?');
        return;
      }

      // 이전에 출제된 문제를 비교후 미출제 영화들만 가져와 다시 저장 
      const unusedMovies = quizMovies.filter(movie => !this.usedQuizIndexes.includes(movie.id));
      if (unusedMovies.length === 0) {
        console.log('해당 장르 영화 출제가 끝났어요~~ 다시 도전해보세요');
        return;
      }
      
      // 랜덤 추출
      const randomIndex = Math.floor(Math.random() * unusedMovies.length);
      const randomMovie = unusedMovies[randomIndex];

      // 현재 문제
      this.currentQuiz = randomMovie;
      this.imgSrc = "https://image.tmdb.org/t/p/w500" + this.currentQuiz.poster_path;
      // 출제 되었다고 등록
      this.usedQuizIndexes.push(randomMovie.id);

      console.log(this.currentQuiz.title)
      // 10초 타이머 시작
      this.startTimer(); 
    },

    gameStart() {
      if (this.startCheck) {
        alert('게임이 시작되었습니다. 종료후에 다시 시도해주세요')
        return
      }

      // 게임판 초기화
      this.score = 0
      this.answerCount = 0
      this.myAnswer = ''

      this.startCheck = true;
      this.showStart = true;
      this.showCountdown = -1;
      this.gameOver = false;

      const delay = (duration) => {
        return new Promise((resolve) => {
          setTimeout(resolve, duration);
        });
      };
      
      delay(1000)
        .then(() => {
          this.showStart = false;
          return delay(1000);
        })
        .then(() => {
          this.showCountdown = 3;
          this.countdown = '3';
          return delay(1000);
        })
        .then(() => {
          this.showCountdown = 2;
          this.countdown = '2';
          return delay(1000);
        })
        .then(() => {
          this.showCountdown = 1;
          this.countdown = '1';
          return delay(1000);
        })
        .then(() => {
          this.showCountdown = 0;
          // Start the game

          // 초기화
          this.currentQuizIndex = -1;
          this.usedQuizIndexes = [];

          // 첫번째 문제를 출제
          this.pickRandomMovie(); 
          return;
        });


    },

    // 정답 제출
    submitAnswer() {
      if (this.gameOver) {
        alert('게임 스타트 버튼을 눌러주세요!!') 
        return
      }

      const answer = this.currentQuiz.title.replace(/[^\wㄱ-ㅎㅏ-ㅣ가-힣]/g, '').toLowerCase();
      const myAnswer = this.myAnswer.replace(/[^\wㄱ-ㅎㅏ-ㅣ가-힣]/g, '').toLowerCase();

      if (myAnswer === answer){
        console.log('정답')

        this.answerCount++
        this.score += 10

        // 만약 연속 5개씩 이상 맞추면 추가점수 10, 20, 30점씩 부여

        if (this.answerCount > 0 && this.answerCount % 5 == 0) {
          this.score += 10 * parseInt((this.answerCount + 1) / 5)
        }

        clearInterval(this.timerInterval); // 타이머 재시작
        this.pickRandomMovie(); // 다음 문제 출제
      }else {
        console.log('오답')
        clearInterval(this.timerInterval); // 타이머 종료

        // 점수를 가장 먼저 등록
        this.setScore()

        this.gameOver = true;
        this.startCheck = false;
        this.cardShow = true

      }

      this.myAnswer = ''
    },

    // 줄거리 추출
    overview_q(str) {
      let result = this.currentQuiz.overview;

      if (result.length > 20) {
        result = result.substring(0, 20) + "...";
      }

      console.log(str);
      console.log(result);
      return result;
    },

    toggleFullOverview() {
      this.showFullOverview = !this.showFullOverview;
    },

    startTimer() {
      this.timer = 10; // 타이머 초기화

      this.timerInterval = setInterval(() => {
        this.timer--; // 1초씩 감소
        if (this.timer <= 0) {
          clearInterval(this.timerInterval); // 타이머 종료
          console.log('시간 초과');
          // 시간초과 문제 종료!!
          // 점수를 가장 먼저 등록
          this.setScore()
          
          this.gameOver = true;
          this.startCheck = false;
          this.cardShow = true

        }
      }, 1000);
    },

    flipCard(value) {
      this.isFlipped = value;
    },

    closeCard() {
      this.cardShow = false;
      this.isFlipped = false;
    },

    // 점수 서버에 등록 => 계속 업데이트 해줄거니까 put
    setScore() {
      if(this.user.overview_points < this.score){
        axios({
          method: 'put',
          url: `${API_URL}/accounts/setscore/`,
          data: { username: this.user.username, followers: this.user.followers, overview_points: this.score },
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          }
        })
        .then((res) => {
          console.log(res)

          // 유저가 게임을 참여한 후에 최신화 하기 위함
          this.getUser()
          this.getRank()
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },

    getUser() {
      this.$store.dispatch('getuser')
      this.user = this.$store.state.user
    },

    getRank() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/overview/getrank/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        }
      })
      .then((res) => {
        this.rankUser = res.data.filter(user => user.overview_points > 0);
        console.log(this.rankUser)
      })
      .catch((err) => {
        console.log(err)
      })
    },


    getImageSrc(base64String) {
      return `data:image/png;base64, ${base64String}`; // Base64 데이터를 이미지 src 형식으로 변환
    },

  },

  computed: {
    selectedGenreTitle() {
      const selectedGenre = this.genereOptions.find(option => option.value === this.genreSelected);
      return selectedGenre ? selectedGenre.text : '';
    },

    rank2users() {
      if (this.rankUser > 1){
        return this.rankUser.slice(1);
      }
      return null
    },

    truncatedOverview() {
      const maxLength = 20;
      if (this.currentQuiz && this.currentQuiz.overview.length > maxLength) {
        if (this.showFullOverview) {
          return this.currentQuiz.overview;
        } else {
          return this.currentQuiz.overview.substring(0, maxLength) + "...";
        }
      }
      return this.currentQuiz.overview;
    },
  },
  created() {
    this.filteredMovies(),
    this.getUser(),
    this.getRank()
  }
}
</script>

<style scoped>
.start-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 4rem;
  animation: startAnimation 1s ease-in-out;
}

.countdown-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 4rem;
  animation: countdownAnimation 1s ease-in-out;
}

.quiz-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 4rem;
}

.game-over-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 4rem;
  color: red;
  animation: gameoverAnimation 1s ease-in-out;
}

@keyframes gameoverAnimation {
  0% {
    transform: translate(-50%, -50%) scale(0);
    opacity: 0;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.5);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

@keyframes startAnimation {
  0% {
    transform: translate(-50%, -50%) scale(0);
    opacity: 0;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.5);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

@keyframes countdownAnimation {
  0% {
    transform: translate(-50%, -50%) scale(0);
    opacity: 0;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.5);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

.timer {
  position: absolute;
  top: 34%;
  right: 20%; /* 원하는 오른쪽 여백 조정 */
  transform: translate(0, -50%);
  font-size: 3rem;
  color: white;
}

.score-text {
  position: absolute;
  top: 36%;
  right: 70%;
  transform: translate(0, -50%);
  font-size: 1rem;
  color: white;
}

.answer-card-container {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.answer-card {
  width: 300px;
  height: 200px;
  position: relative;
  perspective: 1000px;
  transition: transform 0.5s;
  transform-style: preserve-3d;
}

.flipped {
  transform: rotateY(180deg);
}

.front,
.back {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  backface-visibility: hidden;
}

.back {
  transform: rotateY(180deg);
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.back button {
  padding: 10px 20px;
}

.front h2,
.back button {
  margin: 0;
}


body{
    margin-top:20px;
    background:#FAFAFA;
}

.profile-card{
  background: linear-gradient(to bottom, rgba(39,170,225,.8), rgba(28,117,188,.8));
  background-size: cover;
  width: 100%;
  min-height: 90px;
  border-radius: 4px;
  padding: 10px 20px;
  color: #fff;
}

.profile-card img.profile-photo{
  border: 7px solid #fff;
  float: left;
  margin-right: 20px;
  position: relative;
  height: 70px;
  width: 70px;
  border-radius: 50%;
}

.profile-card h5 a{
  font-size: 15px;
}

.profile-card a{
  font-size: 12px;
}

</style>