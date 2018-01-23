<template>
  <div class="main-container">
    <h1>Welcome to Chatire!</h1>
    <div class="">
      <div>
        <div class="tabs">
          <button @click="tab=true" :class="{activy: tab}">Sign Up</button>
          <button @click="tab=false" :class="{activy: !tab}">Sign In</button>
        </div>

        <div>
          <div>
            <form class="vform" v-show="tab" @submit.prevent="signUp">
              <div>
                <input v-model="email" type="email" placeholder="Email Address" required>
              </div>
              <div>
                <div>
                  <input v-model="username" type="text" placeholder="Username" required>
                </div>
                <div>
                  <input v-model="password" type="password" placeholder="Password" required>
                </div>
              </div>
              <input type="checkbox" required>
              <label>
                    Accept terms and Conditions
              </label>
              <button class="sform" type="submit">Sign up</button>
            </form>
          </div>

          <div>
            <form class="vform" v-show="!tab"  @submit.prevent="signIn">
              <div>
                <input v-model="username" type="text" placeholder="Username" required>
              </div>
              <div>
                <input v-model="password" type="password" placeholder="Password" required>
              </div>
              <button class="sform" type="submit">Sign in</button>
            </form>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
  export default {

    data () {
      return {
        email: '',
        username: '',
        password: '',
        tab: true,
      }
    },
    methods: {
      signUp () {
        axios.post('http://127.0.0.1:8080/auth/users/create/', {
          email: this.email,
          username: this.username,
          password: this.password,
        }).then( function (data) {
          console.log(data)
          alert('Your account has been created. You will be signed in automatically')

        }).catch( function (error) {
          console.log(error)
        })
      },
      signIn () {
        console.log(this)
        const creds = {username: this.username, password: this.password}
        const tmp_router = this.$router
        axios.post('http://127.0.0.1:8080/auth/token/create/', creds).then( data => {
          sessionStorage.setItem('authToken', data.auth_token)
          sessionStorage.setItem('username', this.username)
          this.$router.push('/chats')
        }).catch(function (error) {
          console.log(error)
        })
      },
    }
  }
</script>

<style scoped>
  h1{
    padding: 20px;
  }
  .main-container{
    width: 600px;
    margin: 0 auto;
    background: hsla(255, 60%, 38%, 0.8);
    color: white;
    border-radius: 20px;
  }
  .tabs{
    display: flex;
    margin: 15px auto;
    width: 40%;
    justify-content: space-between;
  }
  .tabs button {
    padding: 10px;
    background-color: #4527A0;
    flex: 0 1 150px;
    border-radius: 5px;
    color: white;
  }
  .activy{
    opacity: 0.8;
  }

  .vform{
    width: 50%;
    margin: 0 auto;
    height: 300px;
  }
.vform div{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}

  .vform div input{
    margin: 2px 0px;
    padding: 10px;
    width: 300px;
    border-radius: 10px;
  }

  .terms {
    display: inline-block;
  }
  form input, label{
    display: inline-block;
    margin: 10px 0px;
  }

  form input{
    padding: 30px;
  }

  .sform{
    display: block;
    padding: 15px;
    background: #4527A0;
    margin: 15px auto;
    width: 300px;
    border-radius: 10px;
    color: white;
  }
</style>
