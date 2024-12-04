open System.Text.RegularExpressions

let readLines filePath = System.IO.File.ReadLines(filePath)

let data = readLines "input.txt"

let rx = Regex("mul\(([0-9]{1,3}),([0-9]{1,3})\)", RegexOptions.Compiled)

let xfrm a b =
    let na = a |> int
    let nb = b |> int
    na * nb

let doShit line =
    let mutable x = 0

    let found =
        seq {
            for m in rx.Matches(line) do
                yield m.Groups[1].Value, m.Groups[2].Value
        }

    found |> Seq.iter (fun (a, b) -> x <- x + (xfrm a b))
    printfn "%d" x

data |> Seq.iter (fun x -> doShit x)
