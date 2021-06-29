import os
import discord
import asyncio
import datetime
import time
import json



async def reload(bat, dir, client, ctx=None):
    os.chdir(dir)
    if ctx != None:
            await ctx.send("Reloding...", delete_after=5)
            await asyncio.sleep(6)
            os.startfile(bat)
            await client.close()
    else:
        os.startfile(bat)
        await client.close()
class admin():
    async def mute(ctx, member, *args, role_add=1, role_remove=1, reason=None, **kwargs):
        if ctx.guild.get_role(role_add) in member.roles:
            await ctx.send(f"{member.mention} is already muted.", delete_after=5)
        else:
            await member.add_roles(ctx.guild.get_role(role_add))
            if role_remove != 1:
                await member.remove_roles(ctx.guild.get_role(role_remove))
            if reason == None:
                await ctx.send(f"{member.mention} has been muted.", delete_after=7)
            else:
                await ctx.send(f"{member.mention} has been muted. \nReason: {reason}", delete_after=7)

    async def unmute(ctx, member, *args, role_add=1, role_remove=1, **kwargs):
        if ctx.guild.get_role(role_remove) not in member.roles:
            await ctx.send(f"{member.mention} is not muted.", delete_after=7)
        else:
            await member.remove_roles(ctx.guild.get_role(role_remove))
            if role_add != 1:
                await member.add_roles(ctx.guild.get_role(role_add))
            await ctx.send(f"{member.mention} is now unmuted.", delete_after=7)

    async def clear(ctx, amount=None):
        if amount == None:
            ammount = 99999999999999999
        limit = datetime.datetime.now() - datetime.timedelta(weeks=2)
        await ctx.message.delete()
        purged = await ctx.channel.purge(limit=ammount ,after=limit)
        purged = len(purged)
        await ctx.send(f'cleared {purged} messages', delete_after=5)
        return purged

    async def kick(ctx, member, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} Reason: {reason}', delete_after=7)

    async def ban(ctx, member, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} Reason: {reason}', delete_after=7)

    async def unban(ctx, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users: 
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.message.delete()
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}', delete_after=7)
            else:
                await ctx.message.delete()
                await ctx.send(f"{member} is not banned.", delete_after=5)
class curse():
    async def add_banned_word(ctx, word, dir):
        os.chdir(dir)
        try:
            if os.path.exists("curses.json"):
                    word = word.lower()
                    guildid = str(ctx.guild.id)
                    with open('curses.json', 'r+') as f:
                        curse_db = json.load(f)
                        word_check = word.replace(" ", "")
                        word_check = word_check.split(",")
                        for x in word_check:
                            if x in curse_db[guildid]["curses"]:
                                await ctx.send(f"{x} is in the list already", delete_after=5)
                                return
                        if "," in word:
                            word = word.replace(" ", "")
                            word = word.split(",")
                            with open('curses.json', 'r+') as f:
                                curse_db = json.load(f)
                                curse_list = curse_db[guildid]["curses"]
                                words = []
                                for x in word:
                                    words.append(x)
                                    if words.count(x) > 1:
                                        await ctx.send("Words cannot be added twice.", delete_after=5)
                                        return
                                for x in words:
                                    curse_list.append(x)
                                f.seek(0)
                                f.write(json.dumps(curse_db))
                                f.truncate()
                        else:
                            with open('curses.json', 'r+') as f:
                                curse_db = json.load(f)
                                curse_list = curse_db[guildid]["curses"]
                                curse_list.append(word)
                                f.seek(0)
                                f.write(json.dumps(curse_db))
                                f.truncate()
            else:
                guildid = str(ctx.guild.id)
                guild_dict = {guildid: {}}
                if "," in word:
                    word = word.replace(" ", "")
                    word = word.split(",")
                    words = []
                    for x in word:
                        words.append(x)
                        if words.count(x) > 1:
                            await ctx.send("Words cannot be added twice.", delete_after=5)
                            return
                    guild_dict[guildid]["curses"] = words
                    with open('curses.json', 'w') as f:
                        json.dump(guild_dict, f)
                else:
                    guild_dict[guildid]["curses"] = [str(word)]
                    with open('curses.json', 'w') as f:
                        json.dump(guild_dict, f)
        except:
                if "," in word:
                    word = word.replace(" ", "")
                    word = word.split(",")
                    words = []
                    for x in word:
                        words.append(x)
                        if words.count(x) > 1:
                            await ctx.send("Words cannot be added twice.", delete_after=5)
                            return
                    with open("curses.json", "r") as f:
                        curse_db = json.load(f)
                        new_guild_dict = {guildid: {"curses": words}}
                        curse_db.update(new_guild_dict)
                    with open("curses.json", "w") as f:
                        json.dump(curse_db, f)
                else:
                    with open("curses.json", "r") as f:
                        curse_db = json.load(f)
                        new_guild_dict = {guildid: {"curses": [str(word)]}}
                        curse_db.update(new_guild_dict)
                    with open("curses.json", "w") as f:
                        json.dump(curse_db, f)


    async def remove_banned_word(ctx, word, dir):
            os.chdir(dir)
            try:
                word = word.lower()
                guildid = str(ctx.guild.id)
                if "," in word:
                    word = word.replace(" ", "")
                    word = word.split(",")                  
                    with open('curses.json', 'r+') as f:
                        curse_db = json.load(f)
                        curse_list = curse_db[guildid]["curses"]
                        for x in word:
                            index = curse_list.index(x)
                            curse_list.pop(index)
                        f.seek(0)
                        f.write(json.dumps(curse_db))
                        f.truncate()
                else:
                    with open('curses.json', 'r+') as f:
                        curse_db = json.load(f)
                        curse_list = curse_db[guildid]["curses"]
                        index = curse_list.index(word)
                        curse_list.pop(index)
                        f.seek(0)
                        f.write(json.dumps(curse_db))
                        f.truncate()
            except:
                await ctx.send("This word is not in the list or a list was never created", delete_after=5)

    async def message_filter(message, dir, admin: int=1):
        if message.author.bot or message.guild is None:
            return
        os.chdir(dir)
        if message.author.bot:
            return
        else:
            if admin != 1:
                adminrole = message.guild.get_role(admin)
                if adminrole in message.author.roles or message.author.top_role.position > adminrole.position or message.author.bot:
                    return
                else:    
                    try:
                        messagecontent = message.content.lower()
                        with open("curses.json", "r") as f:
                            data = json.load(f)
                            words = data[str(message.guild.id)]["curses"]
                        for x in words:
                            if x in messagecontent.split():
                                await message.delete()
                                await message.channel.send("Do not say that here!", delete_after=5)
                    except:
                        return

            else:
                    try:
                        messagecontent = message.content.lower()
                        with open("curses.json", "r") as f:
                            data = json.load(f)
                            words = data[str(message.guild.id)]["curses"]
                        for x in words:
                            if x in messagecontent.split():
                                await message.delete()
                                await message.channel.send("Do not say that here!", delete_after=5)
                    except:
                        return
    async def message_edit_filter(after, dir, admin: int=1):
        if after.author.bot or after.guild is None:
            return
        os.chdir(dir)
        if after.author.bot:
            return
        else:
            if admin != 1:
                adminrole = after.guild.get_role(admin)
                if adminrole in after.author.roles or after.author.top_role.position > adminrole.position or after.author.bot:
                    return
                else:    
                    try:
                        messagecontent = after.content.lower()
                        with open("curses.json", "r") as f:
                            data = json.load(f)
                            words = data[str(after.guild.id)]["curses"]
                        for x in words:
                            if x in messagecontent.split():
                                await after.delete()
                                await after.channel.send("Do not say that here!", delete_after=5)
                    except:
                        return

            else:
                    try:
                        messagecontent = after.content.lower()
                        with open("curses.json", "r") as f:
                            data = json.load(f)
                            words = data[str(after.guild.id)]["curses"]
                        for x in words:
                            if x in messagecontent.split():
                                await after.delete()
                                await after.channel.send("Do not say that here!", delete_after=5)
                    except:
                        return

    async def clear_words(ctx, dir):
        os.chdir(dir)
        try:
            with open('curses.json', 'r+') as f:
                curse_db = json.load(f)
                curses = curse_db[str(ctx.guild.id)]["curses"]
                curses.clear()
                f.seek(0)
                f.write(json.dumps(curse_db))
                f.truncate()
        except:
            await ctx.send("There is not a curse list for this guild. Create one by doing !addword followed by a list of words or a single word.", delete_after=10)
class mute_on_join():
    async def mute_add(ctx, member, dir):
        os.chdir(dir)
        guildid = str(ctx.guild.id)
        member = str(member.id)
        try:
            if os.path.exists("muted.json"):
                with open("muted.json", "r+") as f:
                    muted_db = json.load(f)
                    muted_list = muted_db[guildid]["muted"]
                    muted_list.append(member)
                    f.seek(0)
                    f.write(json.dumps(muted_db))
                    f.truncate()
            else:
                muted_db = {guildid: {}}
                muted_db[guildid]["muted"] = [member]
                with open("muted.json", "w") as f:
                    json.dump(muted_db, f)
        except:
            with open("muted.json", "r") as f:
                        muted_db = json.load(f)
                        new_guild_dict = {guildid: {"muted": [member]}}
                        muted_db.update(new_guild_dict)
            with open("muted.json", "w") as f:
                json.dump(muted_db, f)

    async def mute_remove(ctx, member, dir):
        member = str(member.id)
        guildid = str(ctx.guild.id)
        os.chdir(dir)
        try:
            with open("muted.json", "r+") as f:
                muted_db = json.load(f)
                muted_list = muted_db[guildid]["muted"]
                index = muted_list.index(member)
                muted_list.pop(index)
                f.seek(0)
                f.write(json.dumps(muted_db))
                f.truncate()
        except:
            return

    async def mute_on_join(member, role, dir):
        guildid = str(member.guild.id)
        muted_role = member.guild.get_role(role)
        os.chdir(dir)
        with open("muted.json", "r") as f:
            muted_db = json.load(f)
            muted_list = muted_db[guildid]["muted"]
            if str(member.id) in muted_list:
                await member.add_roles(muted_role)
                return 
class warnings():
    async def warn(ctx, member, dir, reason=None):
        os.chdir(dir)
        reason = str(reason)
        guild = str(ctx.guild.id)
        user = member
        member = str(member.id)
        try:
            if os.path.exists("warnings.json"):
                with open("warnings.json", "r+") as f:
                    warnings_db = json.load(f)
                    warnings_db[guild][member]["number"] = warnings_db[guild][member]["number"] + 1 
                    reason_list = warnings_db[guild][member]["reasons"]
                    reason_list.append(reason)
                    f.seek(0)
                    f.write(json.dumps(warnings_db))
                    f.truncate()
                    await ctx.send(f"{user.mention} has been warned \nReason: {reason}", delete_after=7)
            else:
                warnings_db = {guild: {member: {}}}
                warnings_db[guild][member]["number"] = 1
                warnings_db[guild][member]["reasons"] = [reason]
                with open("warnings.json", "w") as f:
                    json.dump(warnings_db, f)
                await ctx.send(f"{user.mention} has been warned \nReason: {reason}", delete_after=7)
        except:
            try:
                with open("warnings.json", "r") as f:
                    warnings_db = json.load(f)
                    guild_check = warnings_db[guild]
                    guild_exception = False
            except:
                guild_exception = True
            try:
                with open("warnings.json", "r") as f:
                        warnings_db = json.load(f)
                        member_check = warnings_db[guild][member]
                        member_exception = False
            except:
                member_exception = True
            if guild_exception:
                with open("warnings.json", "r") as f:
                    warnings_db = json.load(f)
                    new_guild_dict = {guild: {member: {"number": 1, "reasons": [reason]}}}
                    warnings_db.update(new_guild_dict)
                with open("warnings.json", "w") as f:
                    json.dump(warnings_db, f)
                await ctx.send(f"{user.mention} has been warned \nReason: {reason}", delete_after=7)
                return
            if guild_exception == False and member_exception == True:
                with open("warnings.json", "r") as f:
                    warnings_db = json.load(f)
                    guild_dict = warnings_db[guild]
                    new_member_dict = {member: {"number": 1, "reasons": [reason]}}
                    guild_dict.update(new_member_dict)
                    with open("warnings.json", "w") as f:
                        json.dump(warnings_db, f)
                    await ctx.send(f"{user.mention} has been warned \nReason: {reason}", delete_after=7)
                    return
    async def warnings_list(ctx, member, dir, number=None):
            os.chdir(dir)
            guild = str(ctx.guild.id)
            user = member
            member = str(member.id)
            if number != None:
                if int(number) <= 0:
                    return
            try:
                with open("warnings.json", "r") as f:
                    warnings_db = json.load(f)
                    warnings_number = warnings_db[guild][member]["number"]
                    warnings_number = str(warnings_number)
                    if number == None:
                        reasons_with_numbers = []
                        number_reason = 1
                        for x in warnings_db[guild][member]["reasons"]:
                            reason = x
                            reason_number = f"\n#{number_reason}: {reason}"
                            reasons_with_numbers.append(reason_number)
                            number_reason += 1
                        reasons_and_numbers = "".join(reasons_with_numbers)
                        embed = discord.Embed(title = f"{user.name}#{user.discriminator}'s Warnings", color = 0x0000FF, description = f"{user.mention} has {warnings_number} warning/s {reasons_and_numbers}")
                        await ctx.send(embed=embed, reference = ctx.message.reference or ctx.message)
                    else:
                        number = int(number)
                        index = number - 1
                        warnings_reason = warnings_db[guild][member]["reasons"][index]
                        embed = discord.Embed(title = f"{user.name}#{user.discriminator}'s #{warnings_number} Warning", color = 0x0000FF, description = f"Reason: \n{warnings_reason}")
                        await ctx.send(embed=embed, reference = ctx.message.reference or ctx.message)
            except:
                if number == None:
                    await ctx.send(f"{user.mention} has no warnings", delete_after=5)
                else:
                    await ctx.send(f"{user.mention} does not have that many warnings", delete_after=5)
    async def unwarn(ctx, member, dir, number):
        os.chdir(dir)
        user = member
        guild = str(ctx.guild.id)
        member = str(member.id)
        number = number.lower()
        try:
            if number == "all":
                with open("warnings.json", "r+") as f:
                    warnings_db = json.load(f)
                    warnings_reasons = warnings_db[guild][member]["reasons"]
                    warnings_reasons.clear()
                    warnings_db[guild][member]["number"] = 0
                    f.seek(0)
                    f.write(json.dumps(warnings_db))
                    f.truncate()
                    await ctx.send(f"Cleared {user.mention}'s warnings.", delete_after=7)
                    
            
            else:
                if "," in number:
                    number = number.replace(" ", "")
                    number_list = number.split(",")
                    number_list = list(map(int, number_list))
                    number_list = sorted(number_list, reverse=True)
                    for x in number_list:
                        number = x
                        with open("warnings.json", "r+") as f:
                            warnings_db = json.load(f)
                            warnings_reason = warnings_db[guild][member]["reasons"]
                            index = number - 1
                            warnings_reason.pop(index)
                            warnings_db[guild][member]["number"] = warnings_db[guild][member]["number"] - 1
                            f.seek(0)
                            f.write(json.dumps(warnings_db))
                            f.truncate()
                    number_list = list(map(str, number_list))
                    number_list = ", ".join(number_list)
                    await ctx.send(f"Cleared warnings {number_list} from {user.mention}.", delete_after=7)
                else:
                    number = int(number)
                    with open("warnings.json", "r+") as f:
                        warnings_db = json.load(f)
                        warnings_reason = warnings_db[guild][member]["reasons"]
                        index = number - 1
                        warnings_reason.pop(index)
                        warnings_db[guild][member]["number"] = warnings_db[guild][member]["number"] - 1
                        f.seek(0)
                        f.write(json.dumps(warnings_db))
                        f.truncate()
                        number = str(number)
                        await ctx.send(f"Cleared {user.mention}'s #{number} warning.", delete_after=7)
        except:
            if number == "all":
                await ctx.send(f"{user.mention} has no warnings.", delete_after=5)
            
            else: 
                await ctx.send(f"{user.mention} does not have that many warnings.", delete_after=5) 

        

    async def punish(ctx, member, dir, *args, one=None, two=None, three=None, four=None, five=None, six=None, seven=None, eight=None, nine=None, ten=None, remove_role=None, add_role=None, **kwargs):
                os.chdir(dir)
                memberid = str(member.id)
                guild = str(ctx.guild.id)
                with open("warnings.json", "r") as f:
                    warnings_db = json.load(f)
                    warnings_number = warnings_db[guild][memberid]["number"]
                    if warnings_number == 1:
                        warnings_number_str = one
                        message = "You received your first warning."
                    if warnings_number == 2:
                        warnings_number_str = two
                        message = "You received your second warning."
                    if warnings_number == 3:
                        warnings_number_str = three
                        message = "You received your third warning."
                    if warnings_number == 4:
                        warnings_number_str = four
                        message = "You received your fourth warning."
                    if warnings_number == 5:
                        warnings_number_str = five
                        message = "You received your fith warning."
                    if warnings_number == 6:
                        warnings_number_str = six
                        message = "You received your sixth warning."
                    if warnings_number == 7:
                        warnings_number_str = seven
                        message = "You received your seventh warning."
                    if warnings_number == 8:
                        warnings_number_str = eight
                        message = "You received your eighth warning."
                    if warnings_number == 9:
                        warnings_number_str = nine
                        message = "You received your ninth warning."
                    if warnings_number == 10:
                        warnings_number_str = ten
                        message = "You received your tenth warning."
                    if warnings_number_str == None:
                        return
                    if "temp" in warnings_number_str:
                        pun_time = warnings_number_str[5:]
                        pun, time = pun_time.split("_")
                        time = time.lower()
                        if pun == "ban":
                            if "s" in time:
                                time = int(time[:-1])
                                await member.ban(reason=message)
                                await asyncio.sleep(time)
                                member.unban()
                                return
                            if "m" in time:
                                time = int(time[:-1])*60
                                await member.ban(reason=message)
                                await asyncio.sleep(time)
                                member.unban()
                                return
                            if "h" in time:
                                time = int(time[:-1])*3600
                                await member.ban(reason=message)
                                await asyncio.sleep(time)
                                member.unban()
                                return
                            if "d" in time:
                                time = int(time[:-1])*86400
                                await member.ban(reason=message)
                                await asyncio.sleep(time)
                                member.unban()
                                return
                            
                        else:
                            add_role = ctx.guild.get_role(add_role)
                            if remove_role != None:
                                remove_role = ctx.guild.get_role(remove_role)
                                if add_role in member.roles:
                                    return
                                else:
                                    if "s" in time:
                                        time = int(time[:-1])
                                        await member.add_roles(add_role)
                                        await member.remove_roles(remove_role)
                                        await mute_on_join.mute_add(ctx, member, dir)
                                        await asyncio.sleep(time)
                                        await member.add_roles(remove_role)
                                        await member.remove_roles(add_role)
                                        await mute_on_join.mute_remove(ctx, member, dir)
                                        return
                                    if "m" in time:
                                        time = int(time[:-1])*60
                                        await member.add_roles(add_role)
                                        await member.remove_roles(remove_role)
                                        await mute_on_join.mute_add(ctx, member, dir)
                                        await asyncio.sleep(time)
                                        await member.add_roles(remove_role)
                                        await member.remove_roles(add_role)
                                        await mute_on_join.mute_remove(ctx, member, dir)
                                        return
                                    if "h" in time:
                                        time = int(time[:-1])*3600
                                        await member.add_roles(add_role)
                                        await member.remove_roles(remove_role)
                                        await mute_on_join.mute_add(ctx, member, dir)
                                        await asyncio.sleep(time)
                                        await member.add_roles(remove_role)
                                        await member.remove_roles(add_role)
                                        await mute_on_join.mute_remove(ctx, member, dir)
                                        return
                                    if "d" in time:
                                        time = int(time[:-1])*86400
                                        await member.add_roles(add_role)
                                        await member.remove_roles(remove_role)
                                        await mute_on_join.mute_add(ctx, member, dir)
                                        await asyncio.sleep(time)
                                        await member.add_roles(remove_role)
                                        await member.remove_roles(add_role)
                                        await mute_on_join.mute_remove(ctx, member, dir)
                                        return
                            else:
                                    if "s" in time:
                                        time = int(time[:-1])
                                        await member.add_roles(add_role)
                                        await mute_on_join.mute_add(ctx, member, dir)
                                        await asyncio.sleep(time)
                                        await member.remove_roles(add_role)
                                        await mute_on_join.mute_remove(ctx, member, dir)
                                        return
                                    if "m" in time:
                                        time = int(time[:-1])*60
                                        await member.add_roles(add_role)
                                        await mute_on_join.mute_add(ctx, member, dir)
                                        await asyncio.sleep(time)
                                        await member.remove_roles(add_role)
                                        await mute_on_join.mute_remove(ctx, member, dir)
                                        return
                                    if "h" in time:
                                        time = int(time[:-1])*3600
                                        await member.add_roles(add_role)  
                                        await mute_on_join.mute_add(ctx, member, dir)                                 
                                        await asyncio.sleep(time)
                                        await member.remove_roles(add_role)
                                        await mute_on_join.mute_remove(ctx, member, dir)
                                        return
                                    if "d" in time:
                                        time = int(time[:-1])*86400
                                        await member.add_roles(add_role)
                                        await mute_on_join.mute_add(ctx, member, dir)
                                        await asyncio.sleep(time)                                   
                                        await member.remove_roles(add_role)
                                        await mute_on_join.mute_remove(ctx, member, dir)
                                        return
                    else:
                        if warnings_number_str == "ban":
                            await member.ban(reason=message)
                            return
                        if warnings_number_str == "kick":
                            await member.kick(reason=message)
                            return
                        if warnings_number_str == "mute":
                            add_role = ctx.guild.get_role(add_role)
                            if remove_role != None:
                                remove_role = ctx.guild.get_role(remove_role)
                                if add_role in member.roles:
                                    return
                                else:
                                    await member.add_roles(add_role)
                                    await member.remove_roles(remove_role)
                                    await mute_on_join.mute_add(ctx, member, dir)
                            else:
                                await member.add_roles(add_role)
                                await mute_on_join.mute_add(ctx, member, dir)
                    




                
                
                
                
                

                
                
        
        






    

