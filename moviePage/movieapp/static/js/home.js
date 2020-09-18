// let lastDay = new Date(new Date() - 1000 * 60 * 60 * 24)
//   .toISOString()
//   .substring(0, 10);
// let dateInput = document.querySelector('.todayDateInput');
// dateInput.value = lastDay;
// dateInput.setAttribute('max', lastDay);
let contentsBox = document.querySelector('.contents');
// let BackImg = document.querySelector('#img');
const key = '?key=939b44eaa2fa476e3679af34204fb381';
let movieCodeObject = {};
let movieNameArray = [];
let movieCodeArray = [];
let checkNum = 0;
var testarr = new Array();
var resultArr = new Array();
const clickedSearchBtn = async () => {
  try {
    // if (BackImg.classList.contains('fadeIn')) {
    //   BackImg.classList.replace('fadeIn', 'fadeOut');
    // }
    var getArr = new Array();
    var arr = new Array();
    // const rankObject =
    await giveRankObject().then((test2) => {
      // console.log(test2);
    });
    // console.log(resultArr[0]);
    // console.log(testarr);
    for (var k in getArr) {
      arr.push(k);
    }

    for (var p in arr) {
      throwRankObjectFunc(p);
    }
    // let receivedObject = await throwRankObjectFunc(getArr).then(() => {
    //   if (checkNum == 0) {
    //     // contentsBox.removeChild(BackImg);
    //     checkNum++;
    //   }
    // });
  } catch (error) {
    console.log(`clickedSearchBtn 에러 발생 ${error.name}:${error.message}`);
  } finally {
    console.log('clickedSearchBtn Success');
  }
};
const giveRankObject = async () => {
  try {
    let date = document.todayDateForm.todayDateInput1.value;
    let date2 = document.todayDateForm.todayDateInput2.value;
    let targetDate = date.replaceAll('-', '');
    let targetDate2 = date2.replaceAll('-', '');
    var dateArr = new Array();
    for (var i = targetDate; i <= targetDate2; i++) {
      dateArr.push(i);
    }

    for (var j in dateArr) {
      console.log('j=' + dateArr[j]);
      let targetTodayDate = `&targetDt=${dateArr[j]}`;
      const url =
        'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json' +
        key +
        targetTodayDate;
      const response = await (await fetch(url)).json();
      // const test = response.json();
      // testarr.push();
      let createDiv = document.createElement('div');
      const testfunc = (data) => {
        console.log(data);
        for (let i = 0; i < 10; i++) {
          if (data.boxOfficeResult.dailyBoxOfficeList[i].movieNm == '테넷') {
            let rank = data.boxOfficeResult.dailyBoxOfficeList[i].rank;
            let showBox = document.createElement('h1');
            let text = document.createTextNode(`${rank}위 `);
            contentsBox
              .appendChild(showBox)
              .appendChild(rank)
              .appendChild(text);

            console.log(data.boxOfficeResult.dailyBoxOfficeList[i].rank);
          }
        }
      };
      testfunc(response);
    }
    return await resultArr;
  } catch (error) {
    console.log(`giveRankObject 에러 발생 ${error.name}:${error.message}`);
  } finally {
    console.log('giveRankObject Success');
  }
};
const throwRankObjectFunc = async (data) => {
  try {
    let DtYear = data.boxOfficeResult.showRange.substring(0, 4);
    let DtMonth = data.boxOfficeResult.showRange.substring(4, 6);
    let DtDate = data.boxOfficeResult.showRange.substring(6, 8);
    let dateTitle = document.createTextNode(
      `${DtYear}년 ${DtMonth}월 ${DtDate}일`
    );
    let titleBox = document.createElement('h1');
    let createDiv = document.createElement('div');
    createDiv.classList.add('moviePackage');
    contentsBox
      .appendChild(createDiv)
      .appendChild(titleBox)
      .appendChild(dateTitle);
    for (let i = 0; i < 10; i++) {
      let movieRankJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieNm;
      let movieCodeJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieCd;
      let text = document.createTextNode(`${i + 1}위 ` + movieRankJson);
      let textBox = document.createElement('div');
      contentsBox.appendChild(createDiv).appendChild(textBox).appendChild(text);
      textBox.setAttribute('class', `movieContents`);
      textBox.setAttribute('onclick', 'clickedMovieBtn(this);');
      movieNameArray[i] = `${movieRankJson}`;
      movieCodeArray[i] = `${movieCodeJson}`;
      movieCodeObject[movieNameArray[i]] = `${movieCodeArray[i]}`;
    }
  } catch (error) {
    console.log(`throwRankObject 에러 발생 ${error.name}:${error.message}`);
  } finally {
    console.log('throwRankObjectFunc Success');
  }
};
const clickedMovieBtn = async (clickedValue) => {
  try {
    const showCode = await showMeTheCode(clickedValue);
    const throwMoreInfo = await throwMoreInfoFunc(showCode, clickedValue).then(
      () => {
        let NoMoreThanOne = contentsBox.querySelectorAll('.movieContents');
        for (let i = 0; i < NoMoreThanOne.length; i++) {
          if (NoMoreThanOne[i].childElementCount != 0) {
            NoMoreThanOne[i].toggleAttribute('onclick', '');
          }
        }
      }
    );
  } catch (error) {
    console.log(`clickedMovieBtn 에러 발생 ${error.name}:${error.message}`);
  } finally {
    console.log('clickedMovieBtn Success');
  }
};
const showMeTheCode = async (clickedValue) => {
  try {
    let innerHtml = clickedValue.innerHTML;
    let iWantedValue = innerHtml.slice(3, innerHtml.length + 1);
    let Code = await CodeInMovieObj(iWantedValue);
    let moreInfo = await searchMoreInfo(Code);
    return await moreInfo;
  } catch (error) {
    console.log(`showMeTheCode 에러 발생 ${error.name}:${error.message}`);
  } finally {
    console.log('showMeTheCode Success');
  }
};
const CodeInMovieObj = async (clickedValue) => {
  try {
    let iWantedCode = movieCodeObject[clickedValue];
    return await iWantedCode;
  } catch (error) {
    console.log(`CodeInMovieObj 에러 발생 ${error.name}:${error.message}`);
  } finally {
    console.log('CodeInMovieObj Success');
  }
};
const searchMoreInfo = async (Code) => {
  try {
    let usingCode = `&movieCd=${Code}`;
    const infoUrl =
      'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json' +
      key +
      usingCode;
    const responseInfo = await fetch(infoUrl);
    return await responseInfo.json();
  } catch (error) {
    console.log(`searchMoreInfo 에러 발생 ${error.name}:${error.message}`);
  } finally {
    console.log('searchMoreInfo Success');
  }
};
// const throwMoreInfoFunc = async (info, clickedValue) => {
//   try {
//     let directors = [];
//     let actors = [];
//     let searchDirectors = info.movieInfoResult.movieInfo.directors;
//     let searchActors = info.movieInfoResult.movieInfo.actors;
//     let searchDirectorsNum = Object.keys(searchDirectors).length;
//     let searchActorsNum = Object.keys(searchActors).length;
//     if (searchDirectorsNum == 0) {
//       directors[0] = '미입력 혹은 사람이 아님';
//     } else if (searchDirectorsNum > 2) {
//       for (let i = 0; i < 2; i++) {
//         directors[i] = searchDirectors[i].peopleNm;
//       }
//       actors[2] = ' 이하 생략';
//     } else if (searchDirectorsNum <= 2) {
//       for (let i = 0; i < searchDirectorsNum; i++) {
//         directors[i] = searchDirectors[i].peopleNm;
//       }
//     }
//     if (searchActorsNum == 0) {
//       actors[0] = '미입력 혹은 사람이 아님';
//     } else if (searchActorsNum > 4) {
//       for (let i = 0; i < 4; i++) {
//         actors[i] = ' ' + searchActors[i].peopleNm;
//       }
//       actors[4] = ' 이하 생략';
//     } else if (searchActorsNum <= 4) {
//       for (let i = 0; i < searchActorsNum; i++) {
//         actors[i] = ' ' + searchActors[i].peopleNm;
//       }
//     } else {
//       console.log('누구냐 넌');
//     }
//     let addAnotherP = document.createElement('p');
//     let TextDirectors = document.createTextNode(`감독 : ${directors}`);
//     let TextActors = document.createTextNode(`출연진 : ${actors}`);
//     let br = document.createElement('br');
//     addAnotherP.appendChild(TextDirectors);
//     addAnotherP.appendChild(br);
//     addAnotherP.appendChild(TextActors);
//     addAnotherP.classList.add('info');
//     clickedValue.appendChild(addAnotherP);
//   } catch (error) {
//     console.log(`throwMoreInfoFun 에러 발생 ${error.name}:${error.message}`);
//   } finally {
//     console.log('throwMoreInfoFunc Success');
//   }
// };
function reload() {
  setTimeout(location.reload(), 2000);
}
