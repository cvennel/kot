import React, { Component } from "react";
import "./Gameboard.css";


import GameConsole from "../components/GameConsole/GameConsole"
import DiceRoller from "./../components/Dice/DiceRoller";
import PlayerValues from "./../components/PlayerValues/PlayerValues";
import CardStore from "../components/Cards/CardStore";
import PlayerValuesDisplay from "./../components/PlayerValues/PlayerValueDisplay";

import GameInstance from "./../services/gameService";

export default class GameboardLayout extends Component {
  constructor(props) {
    super(props);

    let userName = "Guest_1234";
    let roomName = "Room_1234";
    if (props.location && props.location.state) {
      userName = props.location.state.username;
      roomName = props.location.state.gameRoom;
    }

    this.state = {
      username: userName,
      gameRoom: roomName,
      loggedIn: true
    };

    GameInstance.connect(this.state.gameRoom);
  }

  render() {
    return (
      <div>
        <br />
        <h4>{this.state.gameRoom}</h4>
        <div>
          <div className="col">
            <CardStore
              currentUser={this.state.username}
              currentRoom={this.state.gameRoom} />
          </div>
        </div>
        <div className="container">
          {this.state.loggedIn ? (
            <div className="row">
              <div className="col-sm">
                <PlayerValuesDisplay
                  currentUser={this.state.username}
                  currentRoom={this.state.gameRoom}
                />
              </div>
              <div className="col-sm">
                <DiceRoller
                  currentUser={this.state.username}
                  currentRoom={this.state.gameRoom}
                />
              </div>
              <div className="col-sm">
                <GameConsole
                  sendMessage={payload => {
                    GameInstance.sendMessage(payload);
                  }}
                  currentUser={this.state.username}
                  currentRoom={this.state.gameRoom}
                />
              </div>
              <div className="col-sm">
                <p>Chatroom Placeholder</p>
              </div>
            </div>
          ) : (
            <p>Please login</p>
          )}
        </div>
      </div>
    );
  }
}
