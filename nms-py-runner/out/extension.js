"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const vscode = require("vscode");
const cp = require("child_process");
const net = require("net");
const fs = require("fs");
function exec(command, options) {
    return new Promise((resolve, reject) => {
        cp.exec(command, options, (error, stdout, stderr) => {
            if (error) {
                reject({ error, stdout, stderr });
            }
            resolve({ stdout, stderr });
        });
    });
}
// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
function activate(context) {
    // Use the console to output diagnostic information (console.log) and errors (console.error)
    // This line of code will only be executed once when your extension is activated
    console.log('Congratulations, your extension "nms-py-runner" is now active!');
    let host = vscode.workspace.getConfiguration('sock').get('host') ?? 'localhost';
    let port = vscode.workspace.getConfiguration('sock').get('port') ?? 9001;
    let console_name = vscode.workspace.getConfiguration('sock').get('consoleName') ?? "SocketServer";
    console.log(console_name);
    let console_output = vscode.window.createOutputChannel(console_name);
    // The command has been defined in the package.json file
    // Now provide the implementation of the command with registerCommand
    // The commandId parameter must match the command field in package.json
    let disposable = vscode.commands.registerCommand('nms-py-runner.run', () => {
        // The code you place here will be executed every time your command is executed
        // Display a message box to the user
        console_output.show(true);
        var currentlyOpenTabfilePath = vscode.window.activeTextEditor?.document.uri.fsPath;
        if (currentlyOpenTabfilePath !== undefined) {
            var data = fs.readFileSync(currentlyOpenTabfilePath);
            var data_len = data.byteLength;
            // if (msg_id != undefined) {
            // 	var id_buffer = Buffer.alloc(4);
            // 	id_buffer.writeInt32LE(msg_id);
            // 	data = Buffer.concat([id_buffer, data]);
            // }
            // TODO: Add other 4 bytes before the actual data with some kind of metadata to indicate data version
            // and origin (ie. here or REPL).
            new Promise(resolve => {
                console.log(`Data is ${data_len} bytes long`);
                let socket = net.connect(port, host, () => resolve(socket));
            }).then((sock) => {
                if (sock instanceof net.Socket) {
                    sock.on('data', (data) => {
                        // vscode.window.showInformationMessage(data.toString());
                        // console.log(data);
                        // let result = data.toString();
                        console_output.append(data.toString());
                        // if (data.byteLength === 6 && data.subarray(4, 6).toString() == "OK") {
                        // 	console.log("Received OK. closing connection")
                        // 	sock.end();
                        // } else {
                        // 	console.log(data.byteLength);
                        // 	console.log(data.subarray(4, 6));
                        // 	sock.end();
                        // }
                        sock.end();
                    });
                    // sock.write(Buffer.concat([size_buffer, data]));
                    sock.write(data);
                    vscode.window.showInformationMessage("SENT A MESSAGE");
                }
            });
            // const cmd = `python -c "open('out.a', 'w').write(open('${fname}', 'r').read())"`
            // // const cmd = `python -c "open('test.file', 'w').write('hi')"`;
            // cp.exec(cmd, { cwd: folder }, (error, stdout, stderr) => {
            // 	if (error) {
            // 		vscode.window.showInformationMessage(`Error! ${error}`);
            // 	} else {
            // 		vscode.window.showInformationMessage(stdout);
            // 		vscode.window.showInformationMessage(`Executed: ${cmd}`);
            // 	}
            // });
        }
    });
    context.subscriptions.push(disposable);
}
exports.activate = activate;
// This method is called when your extension is deactivated
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map