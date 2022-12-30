const fs = require("fs");

const input = fs.readFileSync('24.in','utf-8').split('\n');
const board = input.map((str) => str.replace(/\r/g, ""));

const s = [0,1]
const d = [board.length - 1, board[0].length - 2]

const directions = [[0,0],[-1,0],[+1,0],[0,-1],[0,+1]]
m1 = calculatePath(board, s, d)
m2 = calculatePath(board, d, s, m1)
m3 = calculatePath(board, s, d, m1 + m2)

console.log(m1 + m2 + m3)

t=1
function calculatePath(board, start, end, mo = 0) {
    const h = board.length
    const w = board[0].length

    const timeMap = Array(h).fill().map(() => Array(w).fill(-1))

    timeMap[start[0]][start[1]] = 0
    
    for (let m = 0; timeMap[end[0]][end[1]] === -1; m++) {
        const newBoard = createBoardAfterMove(board, mo + m + 1)
        const update = []

        for (let i = 0; i < h; i++) {
            for (let j = 0; j < w; j++) {
                if (timeMap[i][j] === m) {
                    for (const [di,dj] of directions) {
                        if (newBoard[i + di]?.[j + dj] === '.') {
                            update.push([i + di, j + dj])
                        }    
                    }
                }
            }   
        }
        for (const [i,j] of update) {
            timeMap[i][j] = m + 1
        }
    }
    return timeMap[end[0]][end[1]]
}

function createBoardAfterMove(board, m) {
    const h = board.length
    const w = board[0].length
    
    const newBoard = Array(h).fill().map(() => Array(w).fill())

    for (let i = 0; i < h; i++) {
        for (let j = 0; j < w; j++) {
            newBoard[i][j] = board[i][j] === '#' ? '#' : '.'
        }
    }

    for (let i = 0; i < h; i++) {
        for (let j = 0; j < w; j++) {
            if (board[i][j] === '>') {
                newBoard[i][(j - 1 + m) % (w - 2) + 1] = '>'
            }

            if (board[i][j] === '<') {
                newBoard[i][((j - 1 - m) % (w - 2) + (w - 2)) % (w - 2) + 1] = '<'
            }

            if (board[i][j] === 'v') {
                newBoard[(i - 1 + m) % (h - 2) + 1][j] = 'v'
            }

            if (board[i][j] === '^') {
                newBoard[((i - 1 - m) % (h - 2) + (h - 2)) % (h - 2) + 1][j] = '^'
            }
        }
    }

    return newBoard
}
