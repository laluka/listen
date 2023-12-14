const axios = require("axios");
const { convert } = require("html-to-text");
const OpenAI = require("openai");
const fs = require("fs");
const path = require("path");
const audioconcat = require("audioconcat");

const openai = new OpenAI();
const speechFile = path.resolve("./speech.mp3");

async function main() {
  const response = await axios.get("https://thinkloveshare.com/hacking/kong-konga-exploitation-and-hardening/");
  const text = convert(response.data);
  const chunkSize = 4096;
  const chunks = [];

  // Split text into chunks
  for (let i = 0; i < text.length; i += chunkSize) {
    const chunk = text.slice(i, i + chunkSize);
    chunks.push(chunk);
  }

  // Process each chunk
  for (const [index, chunk] of chunks.entries()) {
    console.log(`Processing chunk ${index + 1} of ${chunks.length}`);
    const mp3 = await openai.audio.speech.create({
      model: "tts-1",
      voice: "onyx",
      response_format: "mp3",
      input: chunk,
    });

    const buffer = Buffer.from(await mp3.arrayBuffer());
    await fs.promises.writeFile(`${speechFile}_${index}`, buffer);
  }

  // Merge audio files
  // After processing each chunk
  console.log(`Merging ${chunks.length} MP3 files`);
  const filesToMerge = chunks.map((_, index) => `${speechFile}_${index}`);
  audioconcat(filesToMerge)
    .concat("final.mp3")
    .on("start", function (command) {
      console.log("ffmpeg process started:", command);
    })
    .on("error", function (err, stdout, stderr) {
      console.error("Error:", err);
      console.error("ffmpeg stderr:", stderr);
    })
    .on("end", function (output) {
      console.error("Audio created in:", output);
    });
}

main();
