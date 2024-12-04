open System.Text.RegularExpressions

let readLines filePath = System.IO.File.ReadLines(filePath)

let data = readLines "input.txt"

let rx =
    Regex("mul\(([0-9]{1,3}),([0-9]{1,3})\)|(don't\(\))|(do\(\))", RegexOptions.Compiled)

let xfrm a b =
    let na = a |> int
    let nb = b |> int
    na * nb

let doShit line =
    let mutable x = 0
    let mutable doInstr = true

    let found =
        seq {
            for m in rx.Matches(line) do
                yield m.Groups
        }

    found
    |> Seq.iter (fun (a) ->
        if a[3].Success then
            doInstr <- false

        if a[4].Success then
            doInstr <- true

        x <-
            if (a[1].Success && a[2].Success && doInstr) then
                x + (xfrm a[1].Value a[2].Value)
            else
                x

    )

    printfn "%d" x

data |> Seq.iter (fun x -> doShit x)
