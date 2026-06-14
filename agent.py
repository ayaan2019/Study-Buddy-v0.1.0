from dotenv import load_dotenv
load_dotenv()

from livekit.agents import JobContext, WorkerOptions, cli

async def entrypoint(ctx: JobContext):
    print("Study Assistant Started!")

    await ctx.connect()

    print("Connected to room!")

    participant = await ctx.wait_for_participant()

    print(f"Student joined: {participant.identity}")

if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint
        )
    )